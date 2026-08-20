import logging

# Konfigurasi dual logger (Terminal Console + File audit.log)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("audit.log", encoding="utf-8")
    ]
)

from core.engine import FrameworkAuditEngine

if __name__ == "__main__":
    logging.info("=== STARTING ENTERPRISE AUDIT FRAMEWORK ===")
    engine = FrameworkAuditEngine()
    engine.execute_pipeline()
    engine.export_and_finalize()
    logging.info("=== AUDIT PROCESS FINISHED SUCCESSFULLY ===")