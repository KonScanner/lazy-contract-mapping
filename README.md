# lazy-contract-mapping

    A scrapy tool for lazy contract mapping

## Getting Started

Install python virtual environment

```sh
make install
```

Source into it

```sh
source .venv/bin/activate
```

Run example script (to test)

```sh
sh scripts/example.sh
```

OR

```sh
python3 -m scrapy crawl -a url=https://docs.radioshack.org/radioshack-defi/links/official-addresses contract_mappings -o contracts.json
```
