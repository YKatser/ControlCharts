[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/YKatser/ControlCharts/blob/main/LICENSE)

# About control charts
Control charts solve univariate and multivariate quality-control (or process-monitoring) problems.

This package is about the use of statistical methods and other problem-solving techniques to improve the quality of the products used by our society. These products consist of manufactured goods such as automobiles, computers, and clothing, as well as services such as the generation and distribution of electrical energy, public transportation, banking, retailing, and health care. Quality improvement methods can be applied to any area within a company or organization, including manufacturing, process development, engineering design, finance and accounting, marketing, distribution and logistics, customer service, and field service of products.

The taxonomy of existing control charts:
![taxonomy](docs/pictures/taxonomy.png)

More useful information one can find in the book "Introduction to Statistical Quality Control" by Douglas C. Montgomery.

# Documentation
The documetation is available at [https://ControlCharts.readthedocs.io/](https://ControlCharts.readthedocs.io/)

# Control charts
1. (tba) Univariate Shewhart statistic

2. Multivariate Hotelling's T-squared statistic [[paper]](https://www.semanticscholar.org/paper/Multivariate-Quality-Control-illustrated-by-the-air-Hotelling/529ba6c1a80b684d2f704a7565da305bb84f14e8)  
Hotelling's statistic is one of the most popular statistical process control techniques. It is based on the Mahalanobis distance.
Generally, it measures the distance between the new vector of values and the previously defined vector of normal values additionally using variances.

3. Multivariate Hotelling's T-squared statistic + Q statistic (SPE index) based on PCA 
[[paper]](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/abs/10.1002/cem.800)  
The combined index is based on PCA.
Hotelling’s T-squared statistic measures variations in the principal component subspace.
Q statistic measures the projection of the sample vector on the residual subspace.
To avoid using two separated indicators (Hotelling's T-squared and Q statistics) for the process monitoring, we use a combined one based on logical or.

4. (tba) Univariate and multivariate EWMA statistics

5. (tba) Univariate and multivariate CUSUM statistics

# Examples
Examples of using control charts for anomaly detection are available in the [examples](examples/) folder.

# License
MIT

# Citation
Please cite our project in your publications if it helps your research.
```
Katser, I., V. Kozitsin, and I. Maksimov. "NPP Equipment Fault Detection Methods." Izvestiya vuzov. Yadernaya Energetika 4 (2019): 5-27.
```
Or in BibTeX format:
```
@article{katser2019npp,
  title={NPP Equipment Fault Detection Methods},
  author={Katser, I and Kozitsin, V and Maksimov, I},
  journal={Izvestiya vuzov. Yadernaya Energetika},
  volume={4},
  pages={5--27},
  year={2019}
}
```