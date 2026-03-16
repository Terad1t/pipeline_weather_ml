from ml.prepare_dataset import load_dataset
from ml.train_model import train
from ml.predict import predict

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():

    logging.info("Iniciando pipeline de ML...")

    logging.info("Preparando dataset...")
    df = load_dataset()
    logging.info(f"Dataset carregado: {df.shape}")

    logging.info("Treinando modelo...")
    train()

    logging.info("Fazendo previsão...")
    prediction = predict()

    logging.info(f" Temperatura prevista: {prediction:.2f}°C")

    logging.info("Pipeline finalizada!")


if __name__ == "__main__":
    main()