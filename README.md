# Learning Disjunction

Author: Masoud Jasbi

A Dissertation Submitted To The Department of Linguistics and the Committee on Graduate Studies of Stanford University.

Citation: Jasbi, Masoud. (2018). Learning Disjunction (Doctoral Dissertation). Stanford University. Retrieved from https://purl.stanford.edu/qz846xz9663.

License: Creative Commons Attribution-Noncommercial 3.0 United States.

## Introduction

I wrote my dissertation using RStudio and `knitr`. Each chapter is in a separate Rmarkdown file (`01-chap1.Rmd` is Chapter 1, `02-chap2.Rmd` is Chapter 2, etc.). The `index.Rmd` file 

## Structure of the Repository

## Reproducibility

To reproduce this project, please follow these steps:

1. Make sure you have [the R programming language](https://www.r-project.org/) and [R Studio](https://www.rstudio.com/) installed. This project used R Version 3.4.3 and R Studio Version 1.1.423.

2. Also have the R packages `rmarkdown` (1.10), `bookdown` (0.7), and `thesisdown` (0.0.2) installed.

3. Install the `childesr` package. [The github repo and instructions are here.](https://github.com/langcog/childesr)

4. Make sure the R packages listed in the "R packages" section below are installed.

5. Make sure you have an updated verison of LaTeX. You can install TeX by visiting the [LaTeX Project website](https://www.latex-project.org/get/).

6. Clone/download the repo here by clicking on the green button "Clone or download" on the right top of this page.

7. On your computer, open the main Rmarkdown file (index.Rmd) and press Knit. 

When the Rmd file renders with no error, you will see a folder created as "_book/". Inside the folder you will find the dissertation pdf file as "thesis.pdf". If you see any errors/problems while reproducing our work or if you have any questions please do not hesitate to contact me. My email is available on my website: [masoudjasbi.com](masoudjasbi.com)

## Session Info

|-------|-----------------|
|setting|value|
|version| R version 3.4.3 (2017-11-30)|
|os | macOS Sierra 10.12.6|
|system|x86_64, darwin15.6.0|
|ui|RStudio|
|language|(EN)|
|collate|en_US.UTF-8|
|tz|America/New_York|
|date|2018-09-18|

## R Packages
|------------|-----------|-----------|
|Package|Version|Date|Source|
|abind|1.4-5|2016-07-21|CRAN (R 3.4.0)|
|assertthat|0.2.0|2017-04-11|
|backports|1.1.2|2017-12-13|
|base64enc|0.1-3|2015-07-28|
|bayesplot|1.6.0|2018-08-02|
|bindr|0.1.1|2018-03-13|
|bindrcpp|0.2.2|2018-03-29|
|binom          * 1.1-1    2014-01-02
|boot             1.3-20   2017-08-06
|bootstrap      * 2017.2   2017-02-27
|bridgesampling   0.5-2    2018-08-19
|brms           * 2.5.0    2018-09-16
|Brobdingnag      1.2-6    2018-08-13
|broom            0.5.0    2018-07-17
|cellranger       1.1.0    2016-07-27
|childesr       * 0.1.0    2017-11-09
|cli              1.0.0    2017-11-05
|clisymbols       1.2.0    2017-05-21
|coda             0.19-1   2016-12-08
|colorspace       1.3-2    2016-12-14
|colourpicker     1.0      2017-09-27
|crayon           1.3.4    2017-09-16
|crosstalk        1.0.0    2016-12-21
|DescTools      * 0.99.25  2018-08-14
|digest           0.6.17   2018-09-12
|dplyr          * 0.7.6    2018-06-29
|DT               0.4      2018-01-30
|dygraphs         1.1.1.6  2018-07-11
|evaluate         0.11     2018-07-17
|expm             0.999-2  2017-03-29
|feather        * 0.3.1    2016-11-09
|forcats        * 0.3.0    2018-02-19
|foreign          0.8-71   2018-07-20
|ggplot2        * 3.0.0    2018-07-03
|ggridges         0.5.0    2018-04-05
|ggthemes       * 4.0.1    2018-08-24
|glue             1.3.0    2018-07-17
|gridExtra        2.3      2017-09-09
|gtable         * 0.2.0    2016-02-26
|gtools           3.8.1    2018-06-26
|haven            1.1.2    2018-06-27
|hms              0.4.2    2018-03-10
|htmltools        0.3.6    2017-04-28
|htmlwidgets      1.2      2018-04-19
|httpuv           1.4.5    2018-07-19
|httr             1.3.1    2017-08-20
|igraph           1.2.2    2018-07-27
|inline           0.3.15   2018-05-18
|irr            * 0.84     2012-07-16
|jpeg           * 0.1-8    2014-01-23
|jsonlite         1.5      2017-06-01
|kableExtra     * 0.9.0    2018-05-21
|knitr          * 1.20     2018-02-20
|later            0.7.4    2018-08-31
|lattice          0.20-35  2017-03-25
|lazyeval         0.2.1    2017-10-29
|lme4           * 1.1-18-1 2018-08-17
|lmerTest       * 3.0-1    2018-04-23
|loo              2.0.0    2018-04-11
|lpSolve        * 5.6.13   2015-09-19
|lubridate      * 1.7.4    2018-04-11
|magrittr       * 1.5      2014-11-22
|manipulate       1.0.1    2014-12-24
|markdown         0.8      2017-04-20
|MASS             7.3-50   2018-04-30
|Matrix         * 1.2-14   2018-04-09
|matrixStats      0.54.0   2018-07-23
|mime             0.5      2016-07-07
|miniUI           0.1.1.1  2018-05-18
|minqa            1.2.4    2014-10-09
|modelr           0.1.2    2018-05-11
|munsell          0.5.0    2018-06-12
|mvtnorm          1.0-8    2018-05-31
|nlme             3.1-137  2018-04-07
|nloptr           1.0.4    2014-08-04
|numDeriv         2016.8-1 2016-08-27
|pillar           1.3.0    2018-07-14
|pkgconfig        2.0.2    2018-08-16
|plyr             1.8.4    2016-06-08
|png            * 0.1-7    2013-12-03
|promises         1.0.1    2018-04-13
|purrr          * 0.2.5    2018-05-29
|R6               2.2.2    2017-06-17
|Rcpp           * 0.12.18  2018-07-23
|readr          * 1.1.1    2017-05-16
|readxl           1.1.0    2018-04-20
|reshape2         1.4.3    2017-12-11
|rlang            0.2.2    2018-08-16
|rmarkdown        1.10     2018-06-11
|rprojroot        1.3-2    2018-01-03
|rsconnect        0.8.8    2018-03-09
|rstan            2.17.3   2018-01-20
|rstantools       1.5.1    2018-08-22
|rstudioapi       0.7      2017-09-07
|rvest            0.3.2    2016-06-17
|scales           1.0.0    2018-08-09
|shiny            1.1.0    2018-05-17
|shinyjs          1.0      2018-01-08
|shinystan        2.5.0    2018-05-01
|shinythemes      1.1.1    2016-10-12
|StanHeaders      2.17.2   2018-01-20
|stringi          1.2.4    2018-07-20
|stringr        * 1.3.1    2018-05-10
|threejs          0.3.1    2017-08-13
|tibble         * 1.4.2    2018-01-22
|tidyboot       * 0.1.1    2018-03-14
|tidyr          * 0.8.1    2018-05-18
|tidyselect       0.2.4    2018-02-26
|tidyverse      * 1.2.1    2017-11-14
|viridisLite      0.3.0    2018-02-01
|withr            2.1.2    2018-03-15
|xml2             1.2.0    2018-01-24
|xtable         * 1.8-3    2018-08-29
|xts              0.11-1   2018-09-12
|yaml             2.2.0    2018-07-25
|zoo              1.8-3    2018-07-16
