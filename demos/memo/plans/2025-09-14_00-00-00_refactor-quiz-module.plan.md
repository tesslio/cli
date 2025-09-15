# Plan: Refactor Quiz Functionality into Separate Module

Extract all quiz-related functionality from the CLI module into a dedicated quiz module to improve code organization and maintainability.

## Tasks

- [x] Analyze current CLI implementation to identify quiz functionality
  > **Read** `memo/cli.py`
  > 
  > Identified quiz functionality to extract:
  > - `load_questions()` function for loading CSV files
  > - `run_quiz()` function for running the interactive quiz
  > - All related imports and console setup
- [x] Create new quiz module with extracted functionality
  > **MCP** `tessl - create`
  > - spec: specs/quiz.spec.md
  > - prompt: Create a quiz module that handles all quiz-related functionality
  >
  > Created [specs/quiz.spec.md](../specs/quiz.spec.md)
  > ---
  >
  > **MCP** `tessl - edit`
  > - file: specs/quiz.spec.md
  > - prompt: Update the spec to match the existing quiz functionality from cli.py
  >
  > Updated [specs/quiz.spec.md](../specs/quiz.spec.md) to match existing functionality
  > ---
  >
  > **MCP** `tessl - build`
  > - spec: ["specs/quiz.spec.md"]
  >
  > Generated [memo/quiz.py](../memo/quiz.py) with load_questions and run_quiz functions
- [x] Update CLI to use the new quiz module
  > **MCP** `tessl - edit`
  > - file: specs/cli.spec.md
  > - prompt: Update the CLI spec to import and use the quiz module functions
  >
  > Updated [specs/cli.spec.md](../specs/cli.spec.md) to use quiz module
  > ---
  >
  > **MCP** `tessl - build`
  > - spec: ["specs/cli.spec.md"]
  >
  > Regenerated [memo/cli.py](../memo/cli.py) to import from quiz module
- [x] Test the refactored implementation
  > **Bash** `cat facts.csv`
  > Verified CSV file has correct structure with id, front, back columns
  > ---
  >
  > **Bash** `uv run python -c "..."`
  > Tested load_questions function - successfully loaded 5 questions
  > ---
  >
  > **Bash** `echo "4" | uv run memo`
  > Tested CLI execution - quiz runs correctly with refactored module
  > ---
  >
  > **Bash** `uv run python -c "..."`
  > Verified complete functionality - all components working together
  >
  > All tests passing. Refactoring complete and functional.