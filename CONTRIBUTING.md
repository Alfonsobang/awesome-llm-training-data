# Contributing

Thanks for helping improve this list. The goal is to keep it useful for practitioners who work on LLM training data quality, annotation systems, preference data, synthetic data, governance, and evaluation.

## Quality Bar

Before submitting a resource, check that it meets the repository quality bar:

- No fake links.
- No private or proprietary resources.
- No low-quality SEO content.
- Prefer active and reproducible resources.
- Prefer resources useful to real LLM data teams.
- Prefer primary sources, official repositories, dataset cards, papers, and standards.
- Do not submit private company data, real user data, or proprietary workflows.
- Include access, license, or usage constraints when they affect practical use.
- Avoid unverifiable claims such as adoption numbers, "best", "leading", or "industry standard" unless the linked source supports them directly.

## Resource Format

Use this format:

```markdown
- [DataTrove](https://github.com/huggingface/datatrove) - Tag: [tool] - Large-scale text data processing framework for LLM corpus preparation.
```

Allowed tags:

- `[tool]`
- `[paper]`
- `[dataset]`
- `[benchmark]`
- `[governance]`
- `[report]`
- `[platform]`

## What Makes a Good Addition

- The resource is public and accessible.
- The link points to an official repository, paper, dataset card, standard, or project page.
- The description explains why the resource matters for LLM data work.
- The resource helps with real workflows such as data collection, cleaning, deduplication, inspection, annotation, preference modeling, synthetic data generation, RAG evaluation, financial-domain evaluation, governance, privacy, or compliance.
- The resource has a clear maintenance signal, stable publication venue, or lasting reference value.

## What Usually Does Not Fit

- Vendor landing pages without useful technical documentation.
- Blog posts that mainly summarize other sources.
- Unlicensed mirrors of datasets or papers.
- Private benchmarks, screenshots, or internal workflow descriptions.
- Resources whose only evidence is popularity, star count, or marketing copy.

## Pull Request Checklist

- [ ] I verified that all links are public and working.
- [ ] I used the required resource format.
- [ ] I selected one of the allowed tags.
- [ ] I avoided private, proprietary, or personal data.
- [ ] I added the resource to the most relevant section.
- [ ] I noted access, license, or usage constraints when relevant.
- [ ] I updated both `README.md` and `README.zh-CN.md` when appropriate.
