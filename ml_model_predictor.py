import logging
from typing import Dict, Optional
import pandas as pd
from sklearn.model_selection import train_test_split

class MLModelPredictor:
    """
    Predicts resource demand and revenue using machine learning models.

    Attributes:
        model (object): Trained machine learning model.
        data (pd.DataFrame): Training data used for model training.
    """

    def __init__(self):
        self.model = None
        self.data = pd.DataFrame()
        logging.basicConfig(
            filename='ml_model_predictor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def train_model(self, training_data: Dict[str, float]) -> None:
        """
        Trains the machine learning model using provided data.

        Args:
            training_data (Dict[str, float]): Data for training.
        
        Raises:
            Exception: If training fails due to unforeseen issues.
        """
        try:
            # Convert dictionary to DataFrame
            self.data = pd.DataFrame(training_data)
            X = self.data.drop('target', axis=1)
            y = self.data['target']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
            self.model.fit(X_train, y_train)
            logging.info(f"Model trained with {len(self.data)} samples.")
        except Exception as e:
            logging.error(f"Training failed: {str(e)}")
            raise

    def predict_revenue(self, resources: Dict[str, float]) -> Optional[float]:
        """
        Predicts revenue based on resource allocation.

        Args:
            resources (Dict[str, float]): Allocated resources.

        Returns:
            Optional[float]: Predicted revenue; None if prediction fails.
        """
        try:
            # Prepare input for prediction
            input_data = pd.DataFrame([resources])
            predicted_value = self.model.predict(input_data)[0]
            logging.info(f"Predicted revenue: {predicted_value}")
            return predicted_value
        except Exception as e:
            logging.error(f"Prediction failed: {str(e)}")
            return None