import pandas as pd

# Load the dataset
file_path = 'path_to_your_dataset.csv'
data = pd.read_csv("linkfire.csv")

# 1. Total Pageview Events and Per Day

# Filtering for pageview events
pageview_events = data[data['event'] == 'pageview']

# Total number of pageview events
total_pageviews = pageview_events.shape[0]

# Number of pageview events per day
pageviews_per_day = pageview_events.groupby('date').size()

print("Total Pageview Events:", total_pageviews)
print("Pageviews per day:", pageviews_per_day)


# 2. Other Recorded Events (clicks, previews, etc.)

# Counting the total occurrences of all events (including clicks and previews)
event_counts = data.groupby('event').size()

print("Event Counts (including clicks, previews, etc.):", event_counts)


# 3. Countries Pageviews Came From

# Counting pageview events by country
pageviews_by_country = pageview_events.groupby('country').size().sort_values(ascending=False)

# Display pageviews by country (no limitation)
print("Pageviews by Country:", pageviews_by_country)


# 4. Overall Click Rate (Clicks/Pageviews)

# Filtering for click events
click_events = data[data['event'] == 'click']

# Total number of click events
total_clicks = click_events.shape[0]

# Overall click rate (clicks/pageviews)
click_rate = total_clicks / total_pageviews

print("Overall Click Rate:", click_rate)


# 5. Click Rate Distribution Across Different Links

# Group by link and calculate the click rate (clicks/pageviews per link)
link_pageviews = pageview_events.groupby('linkid').size()
link_clicks = click_events.groupby('linkid').size()

# Merging the dataframes to calculate click rate per link
click_rate_per_link = pd.DataFrame({
    'pageviews': link_pageviews,
    'clicks': link_clicks
}).fillna(0)

click_rate_per_link['click_rate'] = click_rate_per_link['clicks'] / click_rate_per_link['pageviews']

# Display the click rate for each link
print("Click Rate per Link:")
print(click_rate_per_link.sort_values(by='click_rate', ascending=False))
