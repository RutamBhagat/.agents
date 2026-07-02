# Best Practices

Hono is very flexible. You can structure an app in many different ways.
For medium to large teams, however, consistency matters more than flexibility on paper.

The goal is to keep a Hono backend easy to onboard into, with clear boundaries and strong types, without introducing the ceremony of a framework like NestJS.

## Don't make "Controllers" when possible

When possible, do not create "Ruby on Rails-like Controllers".

```ts
// 🙁
const booksList = (c: Context) => {
  return c.json('list books')
}

app.get('/books', booksList)
```

The main issue is type inference. For example, path parameters cannot be inferred in that extracted handler without adding complex generics.

```ts
// 🙁
const bookPermalink = (c: Context) => {
  const id = c.req.param('id') // Can't infer the path param
  return c.json(`get ${id}`)
}
```

Instead, define handlers directly next to the route when possible.

```ts
// 😃
app.get('/books/:id', (c) => {
  const id = c.req.param('id') // Can infer the path param
  return c.json(`get ${id}`)
})
```

This is the Hono equivalent of a NestJS controller method, but without a controller class.

## Use feature-based route modules for larger apps

For medium to large applications, prefer a feature-based modular monolith.

This is a project structure convention, not a Hono framework feature. It works well with Hono because larger apps can be split into sub-apps and mounted with `app.route()`.

```txt
src/
  modules/
    authors/
      routes.ts
      service.ts
      schema.ts
    books/
      routes.ts
      service.ts
      schema.ts
  app.ts
```

Keep each feature together:

- `routes.ts` defines the Hono routes for that feature
- `schema.ts` defines request and response contracts
- `service.ts` contains business logic that should not depend on Hono

```ts
// modules/authors/routes.ts
import { Hono } from 'hono'

const authors = new Hono()

authors.get('/', (c) => c.json('list authors'))
authors.post('/', (c) => c.json('create an author', 201))
authors.get('/:id', (c) => c.json(`get ${c.req.param('id')}`))

export default authors
```

```ts
// app.ts
import { Hono } from 'hono'
import authors from './modules/authors/routes'
import books from './modules/books/routes'

const app = new Hono()

app.route('/authors', authors)
app.route('/books', books)

export default app
```

This gives you Nest-style discoverability by feature, while staying in Hono's native routing model.

## Keep business logic out of handlers

A route handler should focus on HTTP concerns:

- read params, query, body, headers, and auth context
- validate input
- call business logic
- return an HTTP response

Move business logic into plain functions or services that do not depend on Hono when possible.

```ts
// modules/books/service.ts
export const getBookById = async (id: string) => {
  return { id, title: 'Example Book' }
}
```

```ts
// modules/books/routes.ts
import { Hono } from 'hono'
import { getBookById } from './service'

const books = new Hono()

books.get('/:id', async (c) => {
  const id = c.req.param('id')
  const book = await getBookById(id)
  return c.json(book)
})
```

Do not pass the full Hono `Context` into your service layer unless that code is genuinely HTTP-specific.

## Use typed route contracts at the route boundary

For teams, "typed route contracts" are useful in Hono, but the Hono way is schema-backed validation at the route boundary, not DTO classes everywhere.

Use validators so the route schema becomes the source of truth for:

- runtime validation
- typed access to validated input
- client typing when using Hono RPC patterns

```ts
import { Hono } from 'hono'
import { z } from 'zod'
import { zValidator } from '@hono/zod-validator'

const createBookSchema = z.object({
  title: z.string().min(1),
  authorId: z.string().min(1),
})

const books = new Hono()

books.post(
  '/',
  zValidator('json', createBookSchema),
  async (c) => {
    const input = c.req.valid('json')
    return c.json(input, 201)
  }
)
```

This pattern scales well because new developers can find the contract at the route entry point instead of reconstructing it from types, decorators, and runtime code spread across multiple files.

## `factory.createHandlers()` in `hono/factory`

If you need to extract handlers or share middleware stacks, use `factory.createHandlers()` in [`hono/factory`](/docs/helpers/factory). It preserves type inference better than ad hoc controller functions.

```ts
import { createFactory } from 'hono/factory'
import { logger } from 'hono/logger'

const factory = createFactory()

const middleware = factory.createMiddleware(async (c, next) => {
  c.set('foo', 'bar')
  await next()
})

const handlers = factory.createHandlers(logger(), middleware, (c) => {
  return c.json(c.var.foo)
})

app.get('/api', ...handlers)
```

Use this when extraction helps readability. Do not treat it as a reason to rebuild a controller-heavy architecture.

## Keep dependency direction strict

For medium to large teams, strict dependency direction is a good convention even though Hono does not enforce it.

Prefer this direction:

```txt
routes -> services -> data access / external integrations
```

In practice:

- route modules may import schemas, services, and framework middleware
- services may import domain code, repositories, and shared utilities
- lower layers should not import Hono route modules or depend on Hono `Context`
- avoid feature-to-feature circular imports

This keeps the request path obvious and makes features easier to reason about for new developers.

## If you want to use RPC features

The modular routing approach above also works with Hono RPC patterns, but you should export types intentionally.

```ts
// modules/authors/routes.ts
import { Hono } from 'hono'

const authors = new Hono()
  .get('/', (c) => c.json('list authors'))
  .post('/', (c) => c.json('create an author', 201))
  .get('/:id', (c) => c.json(`get ${c.req.param('id')}`))

export default authors
export type AuthorsAppType = typeof authors
```

```ts
import type { AuthorsAppType } from './modules/authors/routes'
import { hc } from 'hono/client'

const client = hc<AuthorsAppType>('http://localhost')
```

If you compose multiple sub-apps and want one combined app type, chain `app.route()` calls and export the resulting type.

```ts
import { Hono } from 'hono'
import authors from './modules/authors/routes'
import books from './modules/books/routes'

const app = new Hono()

const routes = app.route('/authors', authors).route('/books', books)

export default app
export type AppType = typeof routes
```

For very large applications, prefer splitting RPC clients by feature when possible. This keeps route ownership clear and helps avoid TypeScript type complexity growing too large in one place.
