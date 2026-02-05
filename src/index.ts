#!/usr/bin/env node

import { Command } from "commander";
import { evalCommand } from "./commands/eval";

const program = new Command();

program
  .name("tessl")
  .description("Tessl CLI - Agent Enablement Platform")
  .version("0.1.0");

program.addCommand(evalCommand);

program.parse(process.argv);
