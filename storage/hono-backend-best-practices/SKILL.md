---
name: hono-backend-best-practices
description: Use this skill when the user wants guidance, review criteria, or implementation direction for structuring a Hono backend for medium to large teams. Trigger for requests about Hono architecture, maintainability, onboarding, modular monoliths, route organization, service boundaries, typed route contracts, RPC typing, or adopting NestJS-style best practices without bringing NestJS ceremony into the codebase.
---

# Hono Backend Best Practices

Use this skill when working on a Hono backend that should stay easy to onboard into as the team grows.

## Goal

Keep the backend:

- obvious to navigate
- strongly typed at the route boundary
- modular by feature
- light on ceremony

The target is "NestJS-style clarity without NestJS-style framework overhead."

## Working Rules

### Prefer Hono-native routing

- Define handlers directly next to route definitions when possible.
- Do not default to controller classes.
- If extraction is needed, prefer `createFactory()` and `factory.createHandlers()` over ad hoc controller patterns.

### Prefer feature-based modules

For medium to large apps, organize by feature:

```txt
src/
  modules/
    books/
      routes.ts
      service.ts
      schema.ts
```

- `routes.ts` owns HTTP concerns
- `schema.ts` owns request and response contracts
- `service.ts` owns business logic

Mount feature routers with `app.route()`.

### Keep dependency direction strict

Use this direction:

```txt
routes -> services -> data access / external integrations
```

- Lower layers should not depend on Hono `Context`.
- Avoid circular imports across features.
- Keep framework code at the boundary.

### Use typed route contracts

For Hono, typed contracts should usually mean:

- runtime validation at the route boundary
- inferred types from the schema or validator
- `c.req.valid(...)` for validated access
- exported route/app types for `hc` only when typed clients are useful

Avoid creating DTO classes and separate duplicate interfaces by default.

### Keep RPC typing intentional

- Export route or composed app types when `hc` is part of the design.
- For very large apps, split clients by feature to keep TypeScript complexity under control.

## Review Checklist

When reviewing or designing a Hono backend, check:

- Are routes grouped by feature instead of scattered by technical layer?
- Are handlers kept close to route definitions?
- Is business logic outside handlers?
- Is input validated at the route boundary?
- Are schemas the main contract source instead of duplicated DTO/type layers?
- Does dependency flow move one way from routes inward?
- Is the structure improving onboarding without inventing Nest-like ceremony?

## Reference

For the full reference version of this guidance, read:

- `references/hono-best-practices.md`
