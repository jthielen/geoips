# GitHub Pages Deployment Branch

This branch hosts the deployed documentation for the GeoIPS package, for both released versions and `dev` (the current `main` branch), which is made available at [nrlmmd-geoips.github.io/geoips/](https://nrlmmd-geoips.github.io/geoips/).

Other than initial configuration, this branch should not need to be interacted with directly, but instead via GitHub Actions. Key features of this branch (which primarily are there to enable the version switching functionality of the `sphinx-pydata-theme`) include:
- the `versions.json` file, which must exist at a static location, so that the PyData theme (in each deployed version) can point to it to drive the version switcher.
- `index.html`, which is a simple HTML meta redirect to the latest docs
- the `latest` symlink, which links to whichever version-specific directory is considered latest (and typically ought not point to the `dev` directory)
