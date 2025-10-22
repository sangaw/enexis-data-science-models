import argparse
import subprocess
import sys


def run(cmd: list[str]) -> int:
    process = subprocess.run([sys.executable, *cmd])
    return process.returncode


def main() -> int:
    parser = argparse.ArgumentParser(prog="enexis", description="Project task runner")
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("ingest-entsoe", help="Ingest ENTSO-E data")
    sub.add_parser("ingest-ned", help="Ingest NED data")
    sub.add_parser("ingest-meteo-obs", help="Ingest meteo observations")
    sub.add_parser("ingest-meteo-now", help="Ingest meteo forecast now")
    sub.add_parser("build-master-obs", help="Build master observed dataset")
    sub.add_parser("build-master-preds", help="Build master predictions dataset")
    sub.add_parser("train-models", help="Train models")

    args = parser.parse_args()

    if args.cmd == "ingest-entsoe":
        return run(["-m", "src.data_ingestion.ingest_entsoe"])
    if args.cmd == "ingest-ned":
        return run(["-m", "src.data_ingestion.ingest_ned"])
    if args.cmd == "ingest-meteo-obs":
        return run(["-m", "src.data_ingestion.ingest_meteo_obs"])
    if args.cmd == "ingest-meteo-now":
        return run(["-m", "src.data_ingestion.ingest_meteo_forecast_now"])
    if args.cmd == "build-master-obs":
        return run(["-m", "src.data_master.build_master_observed"])
    if args.cmd == "build-master-preds":
        return run(["-m", "src.data_master.build_master_predictions"])
    if args.cmd == "train-models":
        return run(["-m", "src.models.train_models"])  # renamed above

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
