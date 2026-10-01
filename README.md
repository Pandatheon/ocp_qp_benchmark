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

Run the commands from the repository root, since the dataset collection `ocp_qp_dataset_collection/` is resolved relative to the working directory.

### Run benchmark

```bash
ocp-benchmark -c tests/benchmark.json
```

The configuration JSON has the following keys (see [tests/benchmark.json](tests/benchmark.json) for an example):

| Key | Description |
| --- | --- |
| `test_setting` | Dataset names under `ocp_qp_dataset_collection/` to run, e.g. `["random_qp"]` |
| `test_filter_setting` | Keep only problems whose `meta.json` matches, e.g. `[{"has_slacks": false}]` |
| `test_description` | Label for the test set, used in plots |
| `solver_setting` | List of `{"solver": <name>, "opts": {...}}`; the same solver can appear with different options |
| `eval_solver_names` | Subset of solvers to plot in a second, focused figure |
| `metric` | Metric to plot (default: `runtime_fair`) |
| `compare_sol` | Compare solutions against the reference solution (default: `false`) |

Results are written to `results/qpbenchmark_results.csv` and plots to `figures/`.

### Add problems to dataset

```bash
add-problems /path/to/json/folder --name my_dataset_name
```

Each `.json` file in the folder must be loadable by `AcadosOcpQp.from_json()`. The problems are added to `ocp_qp_dataset_collection/my_dataset_name/` (default name: the folder name). Each problem gets:

- `<problem>.json.zst`: compressed QP data
- `<problem>_meta.json`: problem properties (`N`, `has_slacks`, `has_masks`, `definiteness`, ...), used by `test_filter_setting`
- `<problem>_ref_sol.json.zst`: reference solution from IPOPT (omitted if IPOPT fails)

### Python API

See [src/ocp_qp_benchmark/cli/main.py](src/ocp_qp_benchmark/cli/main.py) for an example of using `TestSet`, `SolverSet`, `Results` and `run` directly.

## Supported Solvers

- `PARTIAL_CONDENSING_HPIPM`
- `FULL_CONDENSING_HPIPM`
- `FULL_CONDENSING_QPOASES`
- `FULL_CONDENSING_DAQP`
- `PARTIAL_CONDENSING_OSQP`
- `PARTIAL_CONDENSING_CLARABEL`
- `IPOPT` (via CasADi; also used to generate reference solutions)
