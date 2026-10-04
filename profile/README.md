<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/hsborges-msr/.github/main/assets/wordmark.svg">
    <img alt="hsborges / msr" src="https://raw.githubusercontent.com/hsborges-msr/.github/main/assets/wordmark-light.svg" width="420">
  </picture>
</p>

<p align="center">
  Tools, datasets and studies for <b>mining software repositories</b>:<br>
  GitHub, GitLab, package registries, Q&amp;A sites and beyond.
</p>

## What's here

### Data collection

- [**github-proxy-server**](https://github.com/hsborges-msr/github-proxy-server): proxy for massive data
  collection from the GitHub REST and GraphQL APIs, managing access tokens and requests to stay within the
  API limits.
- [**github-token-donation**](https://github.com/hsborges-msr/github-token-donation): web app where trusted
  people donate GitHub tokens to support our data collection.

### Enrichment

- [**geocoder**](https://github.com/hsborges-msr/geocoder): turns free-form location text, such as what
  developers write on their GitHub profiles, into structured places (city, state, country). Ships as a
  TypeScript library, an HTTP API and a bulk CLI over OpenStreetMap Nominatim, Photon and LocationIQ.
- [**libpostal-rest-docker**](https://github.com/hsborges-msr/libpostal-rest-docker): libpostal address
  parsing as a REST service in a Docker container.

### Archived

- [**repo-insights**](https://github.com/hsborges-msr/repo-insights): web app for visualizing repository
  insights and trends. No longer maintained.

## Donate a token

Large-scale studies quickly hit GitHub's per-token rate limits. If you trust this work, you can donate a token
through [github-token-donation](https://github.com/hsborges-msr/github-token-donation): you authorize a GitHub
OAuth App, see exactly which scopes it requests, and can revoke it at any time in your GitHub settings.

## Contact

Maintained by [Hudson Borges](https://hsborges.dev).
