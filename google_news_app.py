import streamlit as st
import feedparser

st.set_page_config(page_title="Google News Fetcher", page_icon="📰")
st.title("📰 Google News Fetcher")

st.write("Get live news headlines from Google News using RSS feeds.")

# User input
topic = st.text_input("Enter a topic (e.g., technology, sports, India)")

if st.button("Fetch News"):
    if topic.strip():
        url = f"https://news.google.com/rss/search?q={topic.replace(' ', '+')}"
        
        # Parse RSS feed
        feed = feedparser.parse(url)

        if not feed.entries:
            st.warning("No news found for this topic.")
        else:
            st.success(f"Showing latest news for: {topic}")
            st.write("---")
            
            for article in feed.entries[:10]:  # show top 10 results
                st.subheader(article.title)
                st.write(article.published)
                st.write(article.link)
                st.write("---")
    else:
        st.warning("Please type a topic.")
