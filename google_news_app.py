import streamlit as st
import feedparser

st.set_page_config(page_title="Live Google News", page_icon="📰")
st.title("📰 Live Google News App")

st.write("Get the latest news headlines from Google News using RSS feeds.")

# User input
topic = st.text_input("Enter a topic (e.g., technology, sports, India)")

if st.button("Fetch News"):
    if topic.strip():
        # Google News RSS feed URL
        url = f"https://news.google.com/rss/search?q={topic.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
        
        # Parse RSS feed
        feed = feedparser.parse(url)

        if not feed.entries:
            st.warning("No news found for this topic.")
        else:
            st.success(f"Showing latest news for: {topic}")
            st.write("---")
            
            for article in feed.entries[:10]:  # top 10 results
                st.subheader(article.title)
                st.write(f"🗓 Published: {article.published}")
                st.write(f"🔗 [Read more]({article.link})")
                st.write("---")
    else:
        st.warning("Please enter a topic.")
