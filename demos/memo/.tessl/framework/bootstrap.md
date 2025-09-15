# Project Information Bootstrapping

Before you can use any Tessl tools, you need to write information about the project into the AGENTS.md file

Follow these steps:

## 1. Interview

Work out the following information, either by:
a. working out what setup already exists in the directory and confirming it with the user, or 
b. by interviewing the user interactively to work out what they'd like to use:

Cover:
- What stack to use (e.g. Node, TypeScript/ESM, Python, Java/Maven)
- What testing framework to use (you can provide suggestions like `vitest`)
- Where to put specs, code files and test files (e.g. `./specs`, `./src`, `./tests`)
- How to set up the development environment (e.g. environment management and build tools)

Ask these questions one at a time, and ask follow up questions when answers are unclear.

## 2. Setup

Using the supplied information, perform any necessary steps to get the project set up as needed. This might involve creating directories, or installing a minimal set of core dependencies. Consider the local Knowledge Index when selecting dependency versions, if it exists.

## 3. Update Project Configuration

Record the project configuration information in `./AGENTS.md` and remove the "New Project Bootstrapping" section from the file. Make sure to include the test command(s).

When writing up the test command(s), beware of "watch mode" that might interfere with agentic testing feedback loops. For example: the `vitest` command will run in watch mode by default, which will appear to hang as it will not exit - instead the `vitest run` command should be used.

## 4. Interview the user about their task

Before making a spec or making code changes, you should again interview the user about their task.  This time, ask clarifying questions about the details of what they want to build, and the plan to build it.  

Users are generally more successful if:
a. they approach the task in an agile way, building the software in small increments, focussing on one or two files at the most each time.  See if there's a way to start simply and add details about extra features to the plan to be added later, after you get the first slice working.
b. you get feedback from them about the spec before starting to build it.  For example, ask if the test definitions are precise enough, and whether key capabilities are reflected in the spec.

Include steps in your plan for when you need to get feedback from the user.