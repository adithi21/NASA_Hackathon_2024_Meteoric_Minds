## NASA_Hackathon_2024_Meteoric_Minds



#### To Run

streamlit run app.py --server.port 8502


### About Team
Name: Meteoric Minds, 
Members:
1. Lakshmi
2. Adithi
3. Bharath
4. Swastik
5. Vedant
6. Saheer

### Challenge
In this challenge we explored and analysed ground water storage data from NASA – GRACE and GRACE-FO to address the ground water level exhaustion concerns and to take precautions on time. Early warning would also help improve their farming practices. There is heavy dependence on ground water by Indian population both for drinking and farming. 70 to 80% of the Indian farmers depend on ground water. Therefore, to solve this problem, we extracted data specific to India and added Indian states based on longitude and latitude information in the dataset and tried to find trends across states and seasons. Further, we also found that the features surface level soil moisture (sfsm) and root zone soil moisture (rtzsm) are highly correlated with each other and with the target ground water storage. We explored 2 models LSTM and ST-CNN and finally chose ST-CNN because of higher accuracy. The results can be seen in our website.

### Order of Project
1. Combine weekly .nc4 files and roughly get India data: gws_analysis.py
2. Filter data exactly with India shape file and add states:
EDA/EDA_filter_country_add_states.py
3. Perform EDA: EDA/EDA.py
4. Run ML Models: norebooks/*ipynb
5. Run streamlit website: app/pages/forecast.py

