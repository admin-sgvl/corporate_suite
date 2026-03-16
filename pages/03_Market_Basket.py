import streamlit as st
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import plotly.graph_objects as go
import networkx as nx

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="Market Basket Pro", layout="wide")

# --- 1. SIDEBAR GUIDE ---
with st.sidebar:
    st.header("🔍 Analysis Settings")
    st.markdown("""
    **Definitions:**
    - **Support:** How popular an itemset is (0.05 = 5% of all orders).
    - **Confidence:** How likely Item B is purchased when Item A is bought.
    - **Lift:** The strength of the association. Lift > 1 means they are highly related.
    """)
    
    min_support = st.slider("Min Support (Popularity)", 0.01, 0.20, 0.05)
    min_lift = st.slider("Min Lift (Relationship Strength)", 1.0, 5.0, 1.2)
    st.divider()
    st.info("Upload a CSV with 'InvoiceID' and 'ItemName' to begin.")

# --- 2. MAIN INTERFACE ---
st.title("🛒 Market Basket Analysis & Product Web")
st.markdown("Identify cross-selling opportunities by visualizing product purchase correlations.")

uploaded_file = st.file_uploader("Upload Transactional Data (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    
    # Data Validation
    if not all(col in df.columns for col in ['InvoiceID', 'ItemName']):
        st.error("CSV must contain 'InvoiceID' and 'ItemName' columns.")
    else:
        with st.spinner("Processing transactions..."):
            # A. Prepare Data (One-Hot Encoding)
            basket = (df.groupby(['InvoiceID', 'ItemName'])['ItemName']
                      .count().unstack().reset_index().fillna(0)
                      .set_index('InvoiceID'))
            
            def encode_units(x):
                return 1 if x >= 1 else 0
            
            basket_sets = basket.applymap(encode_units)

            # B. Run Association Rules
            frequent_itemsets = apriori(basket_sets, min_support=min_support, use_colnames=True)
            
            if frequent_itemsets.empty:
                st.warning("No frequent itemsets found. Try lowering the 'Min Support' in the sidebar.")
            else:
                rules = association_rules(frequent_itemsets, metric="lift", min_threshold=min_lift)
                
                if rules.empty:
                    st.warning("No strong rules found. Try lowering the 'Min Lift' threshold.")
                else:
                    # Clean up rule strings for display
                    rules["item_a"] = rules["antecedents"].apply(lambda x: ', '.join(list(x)))
                    rules["item_b"] = rules["consequents"].apply(lambda x: ', '.join(list(x)))

                    # C. Metrics Table
                    st.subheader("📊 Association Rules Table")
                    st.dataframe(rules[['item_a', 'item_b', 'support', 'confidence', 'lift']]
                                 .sort_values('lift', ascending=False), use_container_width=True)

                    # D. THE SPIDER-WEB (Network Graph)
                    st.divider()
                    st.subheader("🕸️ Product Connection Web")
                    st.write("Lines indicate items frequently bought together. Node color indicates number of connections.")

                    # Build Graph
                    G = nx.Graph()
                    # Use top 30 rules to keep the web readable
                    top_rules = rules.nlargest(30, 'lift')
                    
                    for _, row in top_rules.iterrows():
                        G.add_edge(row['item_a'], row['item_b'], weight=row['lift'])

                    # Layout (Circular for a spider-web feel)
                    pos = nx.circular_layout(G)

                    # Edge Traces (Lines)
                    edge_x = []
                    edge_y = []
                    for edge in G.edges():
                        x0, y0 = pos[edge[0]]
                        x1, y1 = pos[edge[1]]
                        edge_x.extend([x0, x1, None])
                        edge_y.extend([y0, y1, None])

                    edge_trace = go.Scatter(
                        x=edge_x, y=edge_y,
                        line=dict(width=1, color='#888'),
                        hoverinfo='none', mode='lines'
                    )

                    # Node Traces (Dots)
                    node_x = []
                    node_y = []
                    node_text = []
                    node_adjacencies = []

                    for node, adjacencies in G.adjacency():
                        x, y = pos[node]
                        node_x.append(x)
                        node_y.append(y)
                        node_text.append(f"{node} ({len(adjacencies)} links)")
                        node_adjacencies.append(len(adjacencies))

                    node_trace = go.Scatter(
                        x=node_x, y=node_y,
                        mode='markers+text',
                        text=[n for n in G.nodes()],
                        textposition="top center",
                        hoverinfo='text',
                        marker=dict(
                            showscale=True,
                            colorscale='Viridis',
                            size=25,
                            color=node_adjacencies,
                            colorbar=dict(thickness=15, title='Connectivity', xanchor='left', titleside='right')
                        )
                    )

                    # Final Plotly Figure
                    fig = go.Figure(data=[edge_trace, node_trace],
                                 layout=go.Layout(
                                    showlegend=False,
                                    height=700,
                                    margin=dict(b=20,l=5,r=5,t=40),
                                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                                )
                    
                    st.plotly_chart(fig, use_container_width=True)

                    # E. Export rules
                    st.download_button(
                        label="Download Association Rules CSV",
                        data=rules.to_csv(index=False).encode('utf-8'),
                        file_name='market_basket_rules.csv',
                        mime='text/csv',
                    )
else:
    st.info("👋 Welcome! Upload a transaction CSV to see product associations. Columns should be 'InvoiceID' and 'ItemName'.")
