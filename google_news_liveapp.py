https://news.google.com/rss/search?q=technology&hl=en-US&gl=US&ceid=US:en
pip install feedparser
streamlit
feedparser
pub_date = article.get("published", "No date available")
st.write(f"🗓 Published: {pub_date}")
import streamlit as st
import feedparser

st.set_page_config(page_title="Live Google News", page_icon="📰")
st.title("📰 Live Google News App")

topic = st.text_input("Enter a topic (e.g., technology, sports, India)")

if st.button("Fetch News"):
    if topic.strip():
        url = f"https://news.google.com/rss/search?q={topic.replace(' ', '+')}&hl=en-US&gl=US&ceid=US:en"
        feed = feedparser.parse(url)

        if not feed.entries:
            st.warning("No news found for this topic.")
        else:
            st.success(f"Showing latest news for: {topic}")
            st.write("---")
            
            for article in feed.entries[:10]:  # top 10
                title = article.get("title", "No title")
                link = article.get("link", "#")
                pub_date = article.get("published", "No date available")
                
                st.subheader(title)
                st.write(f"🗓 Published: {pub_date}")
                st.write(f"🔗 [Read more]({link})")
                st.write("---")
    else:
        st.warning("Please enter a topic.")

