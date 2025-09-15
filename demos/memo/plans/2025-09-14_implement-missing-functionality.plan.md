# Plan: Implement Missing Memo Functionality

Complete the memo spaced repetition quiz application by implementing the data layer, SRS algorithm, and integrating all components.

## Overview

Based on the README and existing specs, the following functionality needs to be implemented:
1. Database layer (SQLite) for persistent storage
2. Spaced Repetition System (SRS) using SM2 algorithm (Python port from sm2.js)
3. Update quiz module to work with database
4. Update CLI to support all commands (add cards, review, CSV import)
5. Update MCP server with all tools (get_next_question, save_score, add_card, import_cards)

## Tasks

### Phase 1: Data Layer

- [ ] Create database spec (db.spec.md) with Card model and repository
  - SQLite database with cards table
  - Card model: id, front, back, repetition, easiness, interval, next_date, created_at, updated_at
  - Repository pattern for CRUD operations
  - Methods: create_card, get_card, update_card, get_due_cards, import_from_csv

- [ ] Build database implementation from spec { @user }

- [ ] Interview user to determine testing plan

### Phase 2: Spaced Repetition Algorithm

- [ ] Create SRS spec (srs.spec.md) based on sm2.js
  - Port SM2 algorithm to Python
  - Calculate next review date based on grade (0-5)
  - Update card's repetition, easiness, and interval
  - Return updated scheduling parameters

- [ ] Build SRS implementation from spec

- [ ] Test SRS algorithm with various grades

### Phase 3: Update Quiz Module

- [ ] Edit quiz.spec.md to integrate with database
  - Load due cards from database instead of CSV
  - Update card scheduling after each answer
  - Support configurable number of cards to review

- [ ] Build updated quiz implementation

- [ ] Test quiz with database integration

### Phase 4: Update CLI

- [ ] Edit cli.spec.md to add all commands
  - Main command: review cards (with --cards parameter)
  - Add command: add single card (--front, --back)
  - Add command: import from CSV (--csv)
  - Integrate with database and SRS

- [ ] Build updated CLI implementation

- [ ] Test all CLI commands

### Phase 5: Update MCP Server

- [ ] Edit mcp_server.spec.md to implement all tools
  - get_next_question: return next due card from database
  - save_score: update card with grade and SRS calculation
  - add_card: add new card to database
  - import_cards: bulk import from CSV

- [ ] Build updated MCP server implementation

- [ ] Test MCP server tools

### Phase 6: Integration Testing

- [ ] Run full integration tests
- [ ] Fix any remaining issues
- [ ] Verify all functionality works as described in README

## Key Implementation Details

- **Database**: SQLite with single cards table
- **SRS Algorithm**: Direct port of sm2.js logic to Python
- **Card Selection**: Select cards where next_date <= today, ordered by next_date
- **Grade Scale**: 0 (wrong) to 5 (effortless)
- **Dependencies**: sqlite3, datetime, math (all built-in)

## User Review Points

- [ ] Review spec decomposition before creating specs { @user }
- [ ] Review database and SRS specs before building { @user }
- [ ] Test full application flow after implementation { @user }