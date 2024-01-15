# Load the tidyverse package
library(tidyverse)

# Create a tibble from the given dataset
data <- only_morganella_metadata

# Split the AR_gene column into separate genes
data <- data %>%
  separate_rows(AR_Genes, sep = ", ") %>%
  filter(AR_Genes != "")

# Count the frequency of each gene in each location
gene_frequency <- data %>%
  group_by(location, AR_Genes) %>%
  summarise(gene_frequency_in_location = n()) %>%
  ungroup()

# Print the resulting tibble
print(gene_frequency)
write_csv(gene_frequency, "D:/Morganella/Morganellagene_frequency.csv")
######Load Library

library(reshape2)
library(circlize)


setwd("D:/Morganella/")
data<- read.csv("genes_freq.csv")
# Create a matrix with gene frequencies for each location
mat <- acast(data, location ~ AR_Genes, value.var = "gene_freq", fill = 0)
mat
####Cord##########
#colors <- c(Col1 = "lightgrey", Col2 = "grey",
            Col3 = "darkgrey", Row1 = "#FF410D",
            Row2 = "#6EE2FF", Row3 = "#F7C530",
            Row4 = "#95CC5E", Row5 = "#D0DFE6")

chordDiagram(mat)
circos.clear()