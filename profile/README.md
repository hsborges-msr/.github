<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/hsborges-msr/.github/main/assets/wordmark.svg">
    <img alt="hsborges / msr" src="https://raw.githubusercontent.com/hsborges-msr/.github/main/assets/wordmark-light.svg" width="420">
  </picture>
</p>

<p align="center">
  Tools and datasets for <b>mining software repositories</b>.
</p>

## Projects

### Data collection

- [**github-proxy-server**](https://github.com/hsborges-msr/github-proxy-server): a proxy for collecting
  large amounts of data from the GitHub REST and GraphQL APIs. It rotates tokens so you stay under the rate
  limits.
- [**github-token-donation**](https://github.com/hsborges-msr/github-token-donation): a small web app where
  people can donate GitHub tokens for our research.

### Enrichment

- [**geocoder**](https://github.com/hsborges-msr/geocoder): converts location text, like what people write
  on their GitHub profiles, into city, state and country. Available as a TypeScript library, an HTTP API and
  a CLI.
- [**libpostal-rest-docker**](https://github.com/hsborges-msr/libpostal-rest-docker): libpostal address
  parsing as a REST service in Docker.
- [**github-country-classifier**](https://github.com/hsborges-msr/github-country-classifier): guesses a
  GitHub user's country from their public profile. Runs offline in Node or the browser.
  [Demo](https://hsborges-msr.github.io/github-country-classifier/).

### Archived

- [**repo-insights**](https://github.com/hsborges-msr/repo-insights): a web app for exploring repository
  trends. No longer maintained.

## Donate a token

Big studies run into GitHub's rate limits fast. If you'd like to help, you can donate a token through
[github-token-donation](https://github.com/hsborges-msr/github-token-donation). You can see the requested
scopes before authorizing, and revoke access anytime in your GitHub settings.

## Contact

Maintained by [Hudson Borges](https://hsborges.dev).
