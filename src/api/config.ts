import Conf from "conf";
import { ApiConfig } from "../types";

const config = new Conf<{ apiKey?: string; baseUrl?: string }>({
  projectName: "tessl",
});

const DEFAULT_BASE_URL = "https://api.tessl.io";

export function getApiConfig(): ApiConfig {
  return {
    baseUrl: config.get("baseUrl") || DEFAULT_BASE_URL,
    apiKey: config.get("apiKey") || process.env.TESSL_API_KEY,
  };
}

export function setApiKey(apiKey: string): void {
  config.set("apiKey", apiKey);
}

export function setBaseUrl(baseUrl: string): void {
  config.set("baseUrl", baseUrl);
}
