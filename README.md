# OCP QP Benchmark

Benchmarking framework for OCP QP solvers using [acados](https://github.com/acados/acados).

## Installation

```bash
git clone https://github.com/acados/ocp_qp_benchmark.git
cd ocp_qp_benchmark
git submodule update --recursive --init
pip install -e .
```

## Usage

### Run benchmark

In order to run the benchmark, a configuration JSON file is needed, please refer to `tests/benchmark.json`.

```bash
ocp-benchmark my_config.json
```
The result will be saved as `csv` file.

### Add problems to dataset

```bash
add-problems /path/to/json/folder --name my_dataset_name
```
The dataset will be added into `ocp_qp_dataset_collection`, each problem folder will contain `meta.json`, `ref_sol.json.zst`, `data.json.zst`.

### Python API

Please check the `src/ocp_qp_benchmark/cli/main.py`

## Supported Solvers

- `PARTIAL_CONDENSING_HPIPM`
- `FULL_CONDENSING_HPIPM`
- `FULL_CONDENSING_QPOASES`
- `FULL_CONDENSING_DAQP`
- `PARTIAL_CONDENSING_OSQP`
- `PARTIAL_CONDENSING_CLARABEL`

## Reference Solver (for reference solution)

 - `IPOPT` 