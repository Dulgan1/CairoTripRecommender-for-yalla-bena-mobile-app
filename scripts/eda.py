import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging as logger
from wordcloud import WordCloud

def load_data(path):
    logger.info("loading the data")
    try:
        return pd.read_csv(path)
    except Exception as e:
        logger.info(f"error occured while loading the data {e}")
def overview_of_the_data(df):
    logger.info("overviewing the data")
    try:
        logger.info(df.head())
        logger.info(df.info())
    except Exception as e:
        logger.error(f"error occured while performing the overview of the data: {e}")
def summary_of_catagorical_columns(df):
    logger.info("summery for catagoricak columns")
    try:
        # Count unique values in each categorical column
        for column in ['Name', 'Type of Activity', 'Location']:
            print(f"Value counts for {column}:\n{df[column].value_counts()}\n")
    except Exception as e:
        logger.error(f"error occured while seeing the summary of catagorical columns {e}")
def visualization(df):
    logger.info("visualizing the data frame")
    try:
        # Set the visual style
        sns.set(style='whitegrid')

        # Count plot for 'Type of Activity'
        plt.figure(figsize=(10, 6))
        sns.countplot(y='Type of Activity', data=df, order=df['Type of Activity'].value_counts().index)
        plt.title('Distribution of Type of Activity')
        plt.xlabel('Count')
        plt.ylabel('Type of Activity')
        plt.show()

        # Count plot for 'Location'
        plt.figure(figsize=(10, 6))
        sns.countplot(y='Location', data=df, order=df['Location'].value_counts().index)
        plt.title('Distribution of Locations')
        plt.xlabel('Count')
        plt.ylabel('Location')
        plt.show()
    except Exception as e:
        logger.error(f"error occured while vicualizing the data {e}")
def word_cloud_for_description(df):
    logger.info("word clouding for description")
    try:
        # Create a word cloud
        text = ' '.join(df['Description'].dropna())
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

        # Display the word cloud
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title('Word Cloud for Activity Descriptions')
        plt.show()
    except Exception as e:
        logger.error("error occured while word cloud for description: {e}")
def correlation_and_relationships(df):
    logger.info("correlation and relationships")
    try:
        # Create a pivot table for Type of Activity and Location
        activity_location = pd.crosstab(df['Type of Activity'], df['Location'])
        print(activity_location)

        # Visualize the pivot table
        plt.figure(figsize=(12, 8))
        sns.heatmap(activity_location, cmap='YlGnBu', annot=True, fmt='d')
        plt.title('Heatmap of Type of Activity vs. Location')
        plt.xlabel('Location')
        plt.ylabel('Type of Activity')
        plt.show()
    except Exception as e:
        logger.info(f"error occured while calculating the correlation")

