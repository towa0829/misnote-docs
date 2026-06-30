# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **design documentation repository** for "misnote" (間違いノートアプリ) — a digital mistake-notebook app targeting elementary/middle/high school students. It allows users to record wrong/difficult questions and schedule spaced-repetition reviews. There is no implementation code here; all files are Markdown design documents.

## Document Map

| File | Contents |
|------|----------|
| `design/overview.md` | App description, feature list, tech stack, system architecture diagram, screen list |
| `design/db-design.md` | Full schema (6 tables), ER relationships, design rationale |
| `design/api-design.md` | REST endpoints, request/response examples, error codes, OpenAPI generator workflow |

## Architecture Summary

**Frontend:** Next.js + TypeScript + Tailwind CSS

**Backend:** FastAPI (Python) + SQLAlchemy ORM + Pydantic validation

**API contract flow:**
1. FastAPI auto-generates `openapi.json` at runtime
2. `openapi-generator-cli` converts it to TypeScript types + fetch client under `frontend/src/generated/`
3. Next.js consumes the generated client — no hand-written fetch calls

**Infrastructure (AWS):** Cognito (auth/JWT) → API Gateway → ECS+Fargate (FastAPI) → RDS PostgreSQL. CloudWatch for logging.

**Auth:** All API requests require `Authorization: Bearer {Cognito JWT}`. Base URL: `https://api.misnote.com/v1`.

## Key DB Design Decisions

- `unit_id` on `questions` is nullable (questions can exist without a unit)
- `mistake_notes` is created automatically when an attempt is marked `is_correct: false`
- `correct_streak` on `mistake_notes` tracks consecutive correct answers; `status` transitions to `mastered` when threshold is reached
- `next_review_at` is user-set (not auto-calculated); `GET /mistake-notes/today` filters by this date
- All PKs are UUIDs; all tables are scoped to `user_id` for data isolation
