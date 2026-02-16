import logging
from typing import Dict, Optional
from datetime import datetime

class ResourceMonitor:
    """
    Monitors available resources and their utilization metrics.

    Attributes:
        resource_usage (Dict[str, float]): Dictionary storing current resource usage percentages.
        last_update_time (datetime): Timestamp of the last update.
    """

    def __init__(self):
        self.resource_usage: Dict[str, float] = {}
        self.last_update_time: Optional[datetime] = None
        logging.basicConfig(
            filename='resource_monitor.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def update_resource_usage(self) -> None:
        """
        Updates resource usage data. Simulates resource monitoring.
        
        Raises:
            Exception: If unable to fetch resource data (simulated scenario).
        """
        try:
            # Simulated resource data retrieval
            self.resource_usage = {
                'CPU': 75.0,
                'Memory': 45.0,
                'Storage': 60.0
            }
            self.last_update_time = datetime.now()
            logging.info("Resource usage updated successfully.")
        except Exception as e:
            logging.error(f"Failed to update resource usage: {str(e)}")
            raise

    def get_resource_usage(self, resource_name: str) -> Optional[float]:
        """
        Returns the current usage percentage of a specified resource.

        Args:
            resource_name (str): Name of the resource to check.

        Returns:
            Optional[float]: Usage percentage if available; None otherwise.
        """
        return self.resource_usage.get(resource_name)