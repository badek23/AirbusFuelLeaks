# Detecting Airbus Fuel Leaks
This project outlines a comprehensive approach to predicting and detecting fuel leakages in aircraft for Airbus, focusing on enhancing safety, reducing maintenance costs, and improving operational efficiency.

Current fuel leak detection in the industry often relies on monitoring fuel volume within tanks. The lack of precision inherent in this approach can make it difficult to identify leaks. The project's objective is to develop a data-driven automatic fuel leak detection model to mitigate these issues and enhance aircraft availability while reducing maintenance costs.

Fuel leak detection is currently performed at different flight phases:
Before the flight, initial fuel calculations are made.
During the flight, regular checks are performed to monitor fuel usage and detect abnormalities.
After the flight, post-flight checks ensure there are no discrepancies in fuel usage data.

Fuel leaks impose significant financial burdens, including Aircraft on Ground (AOG) costs, maintenance expenses, and disruption costs. This report estimates that early detection and prevention of fuel leaks can save approximately $34,405 per aircraft monthly. These savings are derived from reducing AOG incidents and lowering maintenance costs.

We utilized historical datasets containing time-series data from aircraft sensors. We performed rigorous data cleaning to handle null values and focused our analysis on the cruise phase of flights, where conditions are most stable for detecting fuel inconsistencies.

Three main models were considered for anomaly detection: Autoencoders, Isolation Forests and XGBoost. The Autoencoder model, which compresses and reconstructs data to identify anomalies, showed better performance metrics compared to the Isolation Forest and XGboost models. The final Autoencoder model achieved an accuracy of 94.24%, recall of 86.95%, precision of 99.21%, and an F1 score of 92.67.

We propose this model be integrated into a user-friendly dashboard accessible to both aircraft crew and ground staff. Initially, the dashboard will be deployed to pilots on high-risk routes and older aircraft, followed by a fleet-wide rollout after user feedback and with continuous improvement.

Implementing this advanced fuel leak detection system will enhance Airbus's operational efficiency, reduce costs, and improve safety measures. Besides monetary savings, the benefits include increased customer satisfaction, better operational efficiency, and less negative environmental impact through preventing fuel wastage.

