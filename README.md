# SmartLLMRouter
Smart LLM Router — an AI gateway that discovers free OpenRouter models, performs health checks, handles rate limits, and intelligently routes requests to the most reliable LLM with failover and latency-aware selection.


🚀 Smart LLM Router

A Smart LLM Router that dynamically discovers free LLM models from OpenRouter, performs health checks, handles rate limits, and intelligently routes user queries to the most reliable model with automatic failover.

This project demonstrates AI infrastructure engineering concepts such as model orchestration, reliability, and failover routing.

📌 Problem

When building applications using free LLM APIs, developers often face several challenges:

❌ Frequent rate limit errors (429)

❌ Some models suddenly become unavailable

❌ Latency differences across models

❌ Wasted API calls trying to determine which model works

❌ Poor reliability when relying on a single model provider

This makes it difficult to build stable AI applications.

💡 Solution

Smart LLM Router acts as an AI gateway / load balancer for LLMs.

It automatically:

Discovers free LLM models available on OpenRouter

Performs health checks

Filters unhealthy or rate-limited models

Routes requests to the best available model

Provides failover when a model fails

This improves reliability, performance, and cost efficiency when working with multiple AI models

🎯 Features

✔ Automatic discovery of free LLM models
✔ Health monitoring of models
✔ Latency-aware model selection
✔ Automatic failover routing
✔ Manual model selection via dropdown
✔ Caching to reduce API quota usage
✔ Interactive Streamlit dashboard

🏗 Architecture
User
  ↓
Streamlit Dashboard
  ↓
Smart LLM Router
  ├── Model Discovery
  ├── Health Check System
  ├── Model Cache
  ├── Rate Limit Handler
  └── Routing Logic
  ↓
OpenRouter Free LLM Models
