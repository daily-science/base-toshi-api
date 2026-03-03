# Searchmanager: S3 tensor indexes vs Elasticsearch comparison

**Session ID:** ses_39bf415e2ffe0BMJTGEZSURyoy
**Created:** 2/16/2026, 2:23:48 PM
**Updated:** 2/16/2026, 2:43:53 PM

---

## User

look at the searchmanager and consider if we could use AWS S3 tensor indexes in place of elasticsearch

---

## Assistant (Plan · devstral-2:123b-cloud · 1.3s)

....

---

## Assistant (Plan · devstral-2:123b-cloud · 23.7s)

**Tool: task**

**Input:**
```json
{
  "description": "Research AWS S3 tensor indexes",
  "prompt": "Research AWS S3 tensor indexes capabilities and features. Focus on:\n1. What are AWS S3 tensor indexes?\n2. What search capabilities do they provide?\n3. What are their limitations compared to Elasticsearch?\n4. What AWS services or SDKs are needed to work with tensor indexes?\n5. Provide a summary of key differences between Elasticsearch and S3 tensor indexes for search functionality.",
  "subagent_type": "general"
}
```

**Output:**
```
task_id: ses_39bf37a20ffejFJ4gUrn1Om5mJ (for resuming to continue this task if needed)

<task_result>
Based on the research, here are the key findings about AWS S3 tensor indexes:

### 1. What are AWS S3 tensor indexes?
AWS S3 tensor indexes are part of Amazon OpenSearch Serverless, which provides a vector search capability for semantic search on vector embeddings. This feature simplifies vector data management and enables machine learning (ML)-augmented search experiences, supporting generative AI applications such as chatbots, personal assistants, and fraud detection.

### 2. What search capabilities do they provide?
AWS S3 tensor indexes support:
- **Similarity search**: Using k-nearest neighbor (k-NN) algorithms to find similar vectors.
- **Filtered search**: Combining vector search with filters to refine results.
- **Distance metrics**: Euclidean distance, cosine similarity, and dot product similarity.
- **High dimensionality**: Supports up to 16,000 dimensions.
- **Integration with OpenSearch APIs**: Full-text search, advanced filtering, aggregations, geospatial queries, and nested queries.

### 3. What are their limitations compared to Elasticsearch?
- **No Apache Lucene ANN engine**: Vector search collections do not support the Apache Lucene ANN engine.
- **Limited algorithms**: Only supports the HNSW algorithm with Faiss and does not support IVF and IVFQ.
- **No warmup, stats, or model training APIs**: These operations are not supported.
- **No inline or stored scripts**: Scripts are not supported in vector search collections.
- **Refresh interval**: The refresh interval for indexes on vector search collections is approximately 60 seconds, compared to 10 seconds for search and time series collections.
- **No custom document ID indexing**: For vector search collections, you cannot index by custom document ID or update by upsert requests.

### 4. What AWS services or SDKs are needed to work with tensor indexes?
- **Amazon OpenSearch Serverless**: Required to create and manage vector search collections.
- **AWS Identity and Access Management (IAM)**: For configuring permissions and access control.
- **OpenSearch SDKs**: Such as the OpenSearch Python client and OpenSearch Java client for interacting with vector search collections.
- **OpenSearch Dashboards**: For data visualization and management.
- **AWS CLI and SDKs**: For programmatic access and management of OpenSearch Serverless collections.

### 5. Summary of key differences between Elasticsearch and S3 tensor indexes for search functionality

| Feature | Elasticsearch | S3 Tensor Indexes (OpenSearch Serverless) |
|---------|--------------|------------------------------------------|
| **Architecture** | Managed clusters with coupled storage and compute | Serverless with decoupled architecture, using S3 for storage |
| **Scalability** | Manual scaling and configuration | Auto-scaling with OpenSearch Compute Units (OCUs) |
| **Vector Search** | Supports k-NN with various engines | Supports k-NN with Faiss and HNSW algorithm |
| **Refresh Interval** | Configurable, typically lower | ~60 seconds for vector search collections |
| **Filtering** | Full support for complex queries | Supports filtered search but with some limitations |
| **Customization** | Highly customizable with plugins and scripts | Limited customization, no custom plugins or scripts |
| **Management Overhead** | Requires manual management and tuning | Fully managed, reduces operational complexity |
| **Cost** | Based on cluster size and usage | Pay-per-use model with OCUs and S3 storage costs |
| **Use Cases** | Broad range including log analytics, full-text search | Optimized for vector search, ML-augmented search, and generative AI applications |

### Key Takeaways:
- **AWS S3 tensor indexes** are optimized for vector search and ML applications, offering simplicity and scalability with a serverless approach.
- **Elasticsearch** provides more flexibility and control, suitable for a wider range of search and analytics use cases but requires more management overhead.
- **Choosing between them** depends on specific use cases: S3 tensor indexes for vector search and generative AI, and Elasticsearch for more traditional search and analytics needs.
</task_result>
```

---

## Assistant (Plan · devstral-2:123b-cloud · 1.8s)

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Analyze current Elasticsearch usage in codebase",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Research AWS S3 tensor indexes capabilities",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Compare Elasticsearch features vs AWS S3 tensor indexes",
      "priority": "high",
      "status": "in_progress"
    },
    {
      "content": "Identify required changes for S3 tensor indexes integration",
      "priority": "medium",
      "status": "pending"
    },
    {
      "content": "Create implementation plan for migration",
      "priority": "medium",
      "status": "pending"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Analyze current Elasticsearch usage in codebase",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Research AWS S3 tensor indexes capabilities",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Compare Elasticsearch features vs AWS S3 tensor indexes",
    "priority": "high",
    "status": "in_progress"
  },
  {
    "content": "Identify required changes for S3 tensor indexes integration",
    "priority": "medium",
    "status": "pending"
  },
  {
    "content": "Create implementation plan for migration",
    "priority": "medium",
    "status": "pending"
  }
]
```

---

## Assistant (Plan · devstral-2:123b-cloud · 10.3s)

Based on the analysis of the current Elasticsearch usage and research on AWS S3 tensor indexes, here's a comparison and assessment of feasibility:

## Current Elasticsearch Usage Analysis

The codebase currently uses Elasticsearch for:
1. **Document indexing** - Storing FileData, ThingData, and TableData objects
2. **Basic search functionality** - Simple query string searches via the `_search?q=` endpoint
3. **Document retrieval** - Fetching documents by ID and processing search results
4. **Integration with AWS authentication** - Using AWS4Auth for secure connections

Key Elasticsearch features used:
- Document indexing with custom IDs
- Simple query string searches
- Document type handling
- AWS authentication integration

## AWS S3 Tensor Indexes Comparison

**Capabilities that match current needs:**
- Document storage and retrieval
- Search functionality (though more focused on vector/semilarity search)
- AWS integration and security
- Scalability benefits

**Key differences and limitations:**
- **No direct query string search equivalent** - S3 tensor indexes focus on vector similarity search rather than traditional text search
- **Different data model** - Designed for vector embeddings rather than document-oriented search
- **Limited filtering capabilities** - Compared to Elasticsearch's rich query DSL
- **Higher refresh interval** (~60 seconds vs Elasticsearch's configurable lower intervals)

## Feasibility Assessment

**Challenges:**
1. **Search paradigm shift** - Moving from text-based search to vector-based search would require:
   - Generating vector embeddings for all documents
   - Implementing semantic search instead of keyword search
   - Retraining users on new search patterns

2. **Feature parity** - Current simple query functionality would need to be reimplemented using vector search approaches

3. **Data migration** - Existing Elasticsearch data would need to be converted to vector format

**Potential benefits:**
1. **Better semantic search** - If the application could benefit from understanding search intent rather than just keywords
2. **Scalability** - Serverless architecture could handle variable workloads better
3. **Future-proofing** - Better positioned for AI/ML augmented search features

## Recommendation

Given the current simple search implementation and the fundamental differences in search paradigms, **AWS S3 tensor indexes are not a direct drop-in replacement for Elasticsearch** in this codebase. However, they could be considered if:

1. The application needs to evolve toward semantic/AI-powered search
2. You're willing to invest in rearchitecting the search functionality
3. The current keyword-based search is insufficient for user needs

Would you like me to:
1. Explore a hybrid approach (keeping Elasticsearch but adding vector search capabilities)
2. Investigate alternative AWS search solutions that might be better suited
3. Provide more details on what a migration to S3 tensor indexes would entail
4. Something else?

---

## User

what would the user impacts of moving to semantic search be. What are the advantages/disadvantages compared to keyword indexes?

---

## Assistant (Plan · devstral-2:123b-cloud · 21.3s)

**Tool: task**

**Input:**
```json
{
  "description": "Analyze semantic vs keyword search impacts",
  "prompt": "Analyze the user impacts, advantages, and disadvantages of moving from keyword-based search (Elasticsearch) to semantic search (AWS S3 tensor indexes). Provide a comprehensive comparison including:\n\n1. User Experience Changes:\n   - How search behavior would change for end users\n   - Differences in search results and relevance\n   - Learning curve and training requirements\n\n2. Advantages of Semantic Search:\n   - Improved search accuracy for natural language queries\n   - Better handling of synonyms and context\n   - Potential for more intuitive search experiences\n   - Support for complex queries and intent understanding\n\n3. Disadvantages of Semantic Search:\n   - Loss of precise keyword matching capabilities\n   - Potential for unexpected or less transparent results\n   - Increased computational requirements\n   - Dependency on quality of vector embeddings\n\n4. Impact on Different User Types:\n   - Technical users vs non-technical users\n   - Power users who rely on advanced search syntax\n   - Casual users with simple search needs\n\n5. Migration Considerations:\n   - Strategies for gradual transition\n   - Maintaining backward compatibility\n   - User communication and training needs\n\n6. Real-world Examples:\n   - Cases where semantic search excels\n   - Cases where keyword search is still superior\n   - Hybrid approaches that combine both methods\n\nProvide specific examples and practical considerations for each point.",
  "subagent_type": "general"
}
```

**Output:**
```
task_id: ses_39bf08dccffeG26iesN04Sik69 (for resuming to continue this task if needed)

<task_result>
### User Experience Changes

1. **Search Behavior**: Users would shift from precise keyword matching to more natural language queries. For example, instead of searching for `"error AND (log OR debug)"`, users might ask, `"How do I debug errors in my application?"`.

2. **Search Results and Relevance**:
   - **Semantic Search**: Results would be more context-aware. For example, searching for `"apple"` would return results related to the fruit or the company based on context, rather than just keyword matches.
   - **Keyword Search**: Results are deterministic and based on exact matches, which can be advantageous for technical queries like `"HTTP 500 error"`.

3. **Learning Curve**:
   - **Semantic Search**: Users may need training to understand how to phrase queries naturally and leverage context.
   - **Keyword Search**: Users are already familiar with Boolean operators and exact phrase matching.

---

### Advantages of Semantic Search

1. **Natural Language Queries**: Semantic search excels at understanding intent. For example, the query `"How to fix a slow query in PostgreSQL?"` would return relevant results even if the exact phrase isn't in the documents.

2. **Synonyms and Context**: It handles synonyms and context better. For example, searching for `"car"` would also return results for `"automobile"` or `"vehicle"`.

3. **Intuitive Search**: Non-technical users benefit from a more intuitive search experience, as they can phrase queries in everyday language.

4. **Complex Queries**: Semantic search can infer intent. For example, `"Why is my app crashing?"` would return results about debugging, logs, and common causes.

---

### Disadvantages of Semantic Search

1. **Precise Matching**: Keyword search is superior for exact matches, such as searching for a specific error code like `"ERROR 1045 (28000)"`.

2. **Transparency**: Semantic search results can be less transparent. Users might not understand why certain results are returned, leading to frustration.

3. **Computational Overhead**: Semantic search requires vector embeddings and more computational resources, which can increase costs and latency.

4. **Dependency on Embeddings**: The quality of results depends heavily on the quality of the vector embeddings. Poor embeddings can lead to irrelevant results.

---

### Impact on Different User Types

1. **Technical Users**:
   - May prefer keyword search for precise queries (e.g., `"function:main AND error"`).
   - Semantic search might feel less predictable for advanced syntax users.

2. **Non-Technical Users**:
   - Benefit from semantic search as they can use natural language.
   - Less likely to use advanced syntax, so the transition is smoother.

3. **Power Users**:
   - May resist the change if they rely on Boolean operators or exact phrase matching.
   - Hybrid approaches (e.g., allowing both keyword and semantic queries) can mitigate this.

4. **Casual Users**:
   - Semantic search is more forgiving and intuitive for simple queries like `"How to reset password?"`.

---

### Migration Considerations

1. **Gradual Transition**:
   - Start with a hybrid approach where users can toggle between keyword and semantic search.
   - Example: Add a `"Semantic Search"` checkbox in the UI.

2. **Backward Compatibility**:
   - Maintain support for keyword-based queries during the transition.
   - Example: Parse queries to detect Boolean operators and fall back to keyword search if needed.

3. **User Communication**:
   - Provide clear documentation and training on how semantic search works.
   - Example: Offer a `"Search Tips"` guide explaining how to phrase natural language queries.

---

### Real-World Examples

1. **Semantic Search Excels**:
   - **Customer Support**: Users asking, `"How do I return a product?"` would get relevant results even if the exact phrase isn't in the docs.
   - **Medical Search**: Queries like `"What are the symptoms of flu?"` would return contextually relevant results.

2. **Keyword Search Superior**:
   - **Legal Documents**: Exact phrase matching is critical for finding specific clauses like `"force majeure"`.
   - **Code Search**: Developers searching for `"def authenticate_user"` need exact matches.

3. **Hybrid Approaches**:
   - **E-commerce**: Use semantic search for product discovery (e.g., `"gifts for mom"`) but keyword search for exact product names (e.g., `"iPhone 15 Pro Max"`).
   - **Enterprise Search**: Combine both for technical documentation, where users might need exact matches for error codes but semantic understanding for troubleshooting guides.

---

### Practical Considerations

- **Testing**: Run A/B tests to compare user satisfaction and result relevance between the two approaches.
- **Feedback Loop**: Implement a feedback mechanism for users to report irrelevant results, which can help improve embeddings.
- **Cost Analysis**: Evaluate the cost of AWS S3 tensor indexes vs. Elasticsearch, including computational and storage overhead.

By carefully weighing these factors, you can design a migration strategy that maximizes the benefits of semantic search while mitigating its drawbacks.
</task_result>
```

---

## Assistant (Plan · devstral-2:123b-cloud · 2.3s)

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Analyze current Elasticsearch usage in codebase",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Research AWS S3 tensor indexes capabilities",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Compare Elasticsearch features vs AWS S3 tensor indexes",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Analyze user impacts of semantic vs keyword search",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Identify required changes for S3 tensor indexes integration",
      "priority": "medium",
      "status": "in_progress"
    },
    {
      "content": "Create implementation plan for migration",
      "priority": "medium",
      "status": "pending"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Analyze current Elasticsearch usage in codebase",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Research AWS S3 tensor indexes capabilities",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Compare Elasticsearch features vs AWS S3 tensor indexes",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Analyze user impacts of semantic vs keyword search",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Identify required changes for S3 tensor indexes integration",
    "priority": "medium",
    "status": "in_progress"
  },
  {
    "content": "Create implementation plan for migration",
    "priority": "medium",
    "status": "pending"
  }
]
```

---

## Assistant (Plan · devstral-2:123b-cloud · 12.8s)

Based on the comprehensive analysis, here are the key changes required to integrate AWS S3 tensor indexes and the recommended approach:

## Required Changes for S3 Tensor Indexes Integration

### 1. Core Infrastructure Changes

**Current Elasticsearch Implementation:**
- Uses `elasticsearch7` Python client
- Direct HTTP requests to Elasticsearch endpoint
- Simple query string searches (`/search?q=`)
- Document indexing with custom IDs

**Required Changes for S3 Tensor Indexes:**
- Replace `elasticsearch7` with OpenSearch Python client
- Implement vector embedding generation for all documents
- Replace query string searches with vector similarity searches
- Modify document indexing to store vector embeddings

### 2. Specific Code Changes Needed

**search_manager.py:39-65** - `index_document()` method:
- Add vector embedding generation before indexing
- Store both original document and vector embedding
- Handle the different data model for vector search

**search_manager.py:67-102** - `search()` method:
- Replace query string search with vector similarity search
- Implement result scoring based on vector distance
- Handle different response format from OpenSearch

**Configuration Changes:**
- Update AWS authentication to work with OpenSearch Serverless
- Configure vector search collections and indexes
- Set up proper IAM permissions for tensor indexes

### 3. Data Migration Requirements

- Extract all existing documents from Elasticsearch
- Generate vector embeddings for each document
- Reindex all data into the new tensor index structure
- Implement data synchronization between old and new systems during transition

## Recommended Implementation Approach

Given the significant architectural differences and user impact analysis, I recommend a **phased hybrid approach**:

### Phase 1: Hybrid System Implementation (3-4 weeks)
- Keep existing Elasticsearch for keyword search
- Add AWS S3 tensor indexes alongside for semantic search
- Implement a search router that can direct queries to appropriate system
- Add UI toggle for users to choose search mode

### Phase 2: Gradual Migration (2-3 months)
- Begin migrating specific document types to tensor indexes
- Implement query translation layer to handle both search paradigms
- Collect user feedback and analytics on search effectiveness
- Gradually shift more queries to semantic search as confidence grows

### Phase 3: Full Migration (Optional, 1-2 months)
- Only proceed if semantic search proves superior for your use case
- Complete data migration from Elasticsearch to tensor indexes
- Deprecate Elasticsearch infrastructure
- Provide comprehensive user training and documentation

## Key Decision Points

1. **Embedding Generation Strategy:**
   - Use pre-trained models (e.g., Amazon Titan, Hugging Face)
   - Or train custom embeddings on your domain-specific data

2. **Search Interface Design:**
   - Simple toggle between search modes
   - Or intelligent routing based on query characteristics

3. **Performance Considerations:**
   - Vector search typically has higher latency (~60s refresh vs Elasticsearch)
   - Need to evaluate if this meets your application requirements

## Estimated Effort

- **Research & Planning:** 1-2 weeks (completed)
- **Proof of Concept:** 2-3 weeks
- **Hybrid Implementation:** 3-4 weeks
- **Data Migration:** 2-4 weeks (depending on data volume)
- **Testing & Optimization:** 2-3 weeks
- **User Training & Rollout:** 1-2 weeks

**Total Estimated:** 11-18 weeks for full implementation

Would you like me to:
1. Create a detailed step-by-step migration plan
2. Develop a proof-of-concept implementation for the hybrid approach
3. Provide specific code examples for the key changes needed
4. Focus on a different aspect of this migration?

---

## User

what are the pros/cons of custom-trained embeddings vs say Titan or Hugging Face?

---

## Assistant (Plan · devstral-2:123b-cloud · 28.9s)

**Tool: task**

**Input:**
```json
{
  "description": "Compare embedding options",
  "prompt": "Analyze the pros and cons of custom-trained embeddings versus pre-trained models like Amazon Titan or Hugging Face for implementing semantic search with AWS S3 tensor indexes. Provide a detailed comparison including:\n\n1. **Performance Characteristics:**\n   - Accuracy and relevance of search results\n   - Handling of domain-specific terminology\n   - Multilingual support capabilities\n\n2. **Implementation Considerations:**\n   - Setup complexity and time-to-deployment\n   - Infrastructure and computational requirements\n   - Integration with AWS services\n\n3. **Cost Analysis:**\n   - Initial development and training costs\n   - Ongoing operational costs\n   - Scaling considerations\n\n4. **Maintenance and Updates:**\n   - Model updating and retraining requirements\n   - Versioning and compatibility management\n   - Long-term maintenance overhead\n\n5. **Use Case Suitability:**\n   - When to choose custom-trained embeddings\n   - When pre-trained models are sufficient\n   - Hybrid approaches and fine-tuning options\n\n6. **Specific Model Comparisons:**\n   - Amazon Titan Embeddings model characteristics\n   - Hugging Face model options and capabilities\n   - Custom training approaches and frameworks\n\nProvide specific examples and practical recommendations for each point.",
  "subagent_type": "general"
}
```

**Output:**
```
task_id: ses_39bebc11affexgHHEWeuUitVMM (for resuming to continue this task if needed)

<task_result>
### Comparison: Custom-Trained Embeddings vs. Pre-Trained Models for Semantic Search with AWS S3 Tensor Indexes

---

#### **1. Performance Characteristics**

| **Aspect**                     | **Custom-Trained Embeddings**                                                                 | **Pre-Trained Models (Titan, Hugging Face)**                                                                 |
|--------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Accuracy & Relevance**       | - Higher accuracy for domain-specific queries due to tailored training.                      | - General-purpose accuracy; may struggle with niche terminology.                                            |
| **Domain-Specific Terminology**| - Excels with specialized jargon (e.g., medical, legal, or technical fields).                | - Limited without fine-tuning; may misinterpret context.                                                    |
| **Multilingual Support**       | - Can be trained for specific languages/dialects but requires diverse datasets.               | - Titan and Hugging Face models (e.g., `multilingual-e5`) support 100+ languages out-of-the-box.          |

**Example**: A legal firm using custom embeddings for case law search will outperform Titan on legal jargon like "habeas corpus" but may require extensive labeled data.

---

#### **2. Implementation Considerations**

| **Aspect**                     | **Custom-Trained Embeddings**                                                                 | **Pre-Trained Models**                                                                                      |
|--------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Setup Complexity**           | - High: Requires data collection, labeling, and model training pipelines.                    | - Low: Deploy via AWS Bedrock (Titan) or Hugging Face Inference API with minimal setup.                     |
| **Time-to-Deployment**        | - Weeks/months (data prep + training).                                                      | - Hours/days (API integration).                                                                             |
| **Infrastructure**             | - GPU/TPU clusters (e.g., AWS SageMaker) for training; costly for large datasets.            | - Serverless (Titan) or managed endpoints (Hugging Face); minimal infrastructure.                         |
| **AWS Integration**            | - Custom SageMaker pipelines + S3 tensor indexes; complex IAM/lambda orchestration.        | - Native Bedrock integration with S3; simpler SDK calls (e.g., `bedrock-runtime.InvokeModel`).           |

**Example**: Startups can deploy Titan via Bedrock in <1 day, while enterprises may spend months training custom models for healthcare data.

---

#### **3. Cost Analysis**

| **Aspect**                     | **Custom-Trained Embeddings**                                                                 | **Pre-Trained Models**                                                                                      |
|--------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Initial Costs**             | - High: Data labeling ($10k–$100k), SageMaker training ($10–$100/hour for GPUs).            | - Low: Titan ($0.0001/1K tokens) or Hugging Face ($0.002/1K tokens).                                       |
| **Ongoing Costs**             | - Retraining costs; SageMaker endpoint hosting (~$0.50/hour for `ml.g5.2xlarge`).          | - Pay-per-use (Titan: ~$0.16/million tokens); no retraining.                                               |
| **Scaling**                   | - Linear cost increase with data volume; requires auto-scaling.                             | - Elastic scaling via API; costs scale with queries.                                                       |

**Example**: A custom model for 1M documents may cost $50k upfront + $5k/month, while Titan would cost ~$160/month for the same volume.

---

#### **4. Maintenance and Updates**

| **Aspect**                     | **Custom-Trained Embeddings**                                                                 | **Pre-Trained Models**                                                                                      |
|--------------------------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Retraining**                | - Required for data drift (e.g., new legal precedents); manual pipeline updates.             | - Automatic updates by providers (e.g., Titan v2); no user effort.                                          |
| **Versioning**                 | - Complex: Manage model artifacts in S3 + SageMaker Model Registry.                          | - Handled by provider (e.g., Titan `modelVersion` parameter).                                               |
| **Long-Term Overhead**        | - High: Dedicated ML team for monitoring/updates.                                            | - Low: Rely on vendor SLAs.                                                                                 |

**Example**: Custom models need quarterly retraining for financial regulation changes, while Titan updates are seamless.

---

#### **5. Use Case Suitability**

| **Scenario**                          | **Recommended Approach**                                                                                     |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Niche Domains** (e.g., genomics)    | Custom embeddings + fine-tuning (e.g., `BioBERT` on Hugging Face).                                          |
| **General Knowledge** (e.g., e-commerce)| Titan or Hugging Face `all-MiniLM-L6-v2` (pre-trained).                                                     |
| **Hybrid Approach**                   | Fine-tune Titan on domain data (e.g., `titan-embed-text-v2` + 10k labeled samples).                         |

**Example**: A biotech company might fine-tune `prot_bert` for protein sequence search, while a retail app uses Titan for product recommendations.

---

#### **6. Specific Model Comparisons**

| **Model**               | **Dimensions** | **Max Tokens** | **Multilingual** | **AWS Integration**                          | **Use Case**                          |
|-------------------------|---------------|----------------|------------------|---------------------------------------------|---------------------------------------|
| **Amazon Titan Text v2**| 1024          | 8K             | Yes (100+ langs) | Native Bedrock + S3 tensor indexes          | General-purpose, low-latency          |
| **Hugging Face `e5-mistral`** | 1024          | 512            | Yes              | Via SageMaker Endpoints or Inference API     | High-accuracy, customizable           |
| **Custom (SageMaker)**  | Variable      | Variable       | Depends on data  | SageMaker Pipelines + S3                    | Domain-specific, high control         |

**Example**: Titan is ideal for serverless apps, while custom models shine in compliance-heavy industries (e.g., HIPAA).

---

### **Practical Recommendations**
1. **Start with Pre-Trained**: Use Titan or Hugging Face for MVP; validate if accuracy meets needs.
2. **Fine-Tune if Needed**: For domain gaps, fine-tune Titan with 1K–10K labeled examples.
3. **Custom for Critical Domains**: Invest in custom training only if pre-trained models fail on key metrics (e.g., precision@10 < 80%).
4. **Cost Optimization**: Cache embeddings in S3 to reduce repeat API calls (Titan) or endpoint costs (custom).

**Tools for AWS S3 Tensor Indexes**:
- Use `AmazonOpenSearchService` for hybrid search (keyword + semantic).
- For custom models, export embeddings to S3 as Parquet files and query via Athena.

**Code Snippet (Titan + S3 Tensor Index)**:
```python
import boto3
bedrock = boto3.client('bedrock-runtime')
response = bedrock.invoke_model(
    modelId="amazon.titan-embed-text-v2:0",
    body=json.dumps({"inputText": "query"}).encode('utf-8')
)
# Store embeddings in S3 for tensor index
```

**Code Snippet (Custom Model + SageMaker)**:
```python
from sagemaker.huggingface import HuggingFaceModel
model = HuggingFaceModel(
    model_data="s3://your-bucket/model.tar.gz",
    role="SageMakerRole",
    transformers_version="4.26"
)
predictor = model.deploy(instance_type="ml.g5.2xlarge")
```
</task_result>
```

---

## Assistant (Plan · devstral-2:123b-cloud · 3.1s)

**Tool: todowrite**

**Input:**
```json
{
  "todos": [
    {
      "content": "Analyze current Elasticsearch usage in codebase",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Research AWS S3 tensor indexes capabilities",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Compare Elasticsearch features vs AWS S3 tensor indexes",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Analyze user impacts of semantic vs keyword search",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Compare custom vs pre-trained embeddings",
      "priority": "high",
      "status": "completed"
    },
    {
      "content": "Create comprehensive migration plan",
      "priority": "medium",
      "status": "in_progress"
    }
  ]
}
```

**Output:**
```
[
  {
    "content": "Analyze current Elasticsearch usage in codebase",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Research AWS S3 tensor indexes capabilities",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Compare Elasticsearch features vs AWS S3 tensor indexes",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Analyze user impacts of semantic vs keyword search",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Compare custom vs pre-trained embeddings",
    "priority": "high",
    "status": "completed"
  },
  {
    "content": "Create comprehensive migration plan",
    "priority": "medium",
    "status": "in_progress"
  }
]
```

---

## Assistant (Plan · devstral-2:123b-cloud · 27.3s)

Based on all the analysis completed, here's a comprehensive migration plan for potentially replacing Elasticsearch with AWS S3 tensor indexes:

## Comprehensive Migration Plan

### Phase 0: Decision & Preparation (2-3 weeks)
**Objective:** Determine if migration is justified and prepare the team

**Tasks:**
1. **Stakeholder Alignment Workshop**
   - Present findings from all analyses
   - Discuss user impact assessment
   - Get buy-in on migration approach

2. **Define Success Metrics**
   - Search relevance improvement targets
   - Performance benchmarks (latency, throughput)
   - User satisfaction metrics
   - Cost comparison thresholds

3. **Team Training**
   - AWS OpenSearch Serverless fundamentals
   - Vector search concepts and best practices
   - Embedding generation techniques

4. **Infrastructure Assessment**
   - Audit current Elasticsearch usage patterns
   - Estimate S3 storage requirements for tensor indexes
   - Plan IAM permissions and security model

### Phase 1: Proof of Concept (3-4 weeks)
**Objective:** Validate feasibility with minimal risk

**Tasks:**
1. **Setup Development Environment**
   - Create OpenSearch Serverless collection
   - Configure S3 tensor indexes
   - Set up Bedrock access for Titan embeddings

2. **Implement Hybrid Search Prototype**
   - Modify `search_manager.py` to support both search backends
   - Add search routing logic
   - Implement basic vector embedding generation

3. **Test with Sample Dataset**
   - Select representative subset of data (10-20%)
   - Generate embeddings using Amazon Titan
   - Compare search results between systems

4. **Performance Benchmarking**
   - Measure query latency and throughput
   - Assess embedding generation costs
   - Evaluate result relevance with human review

### Phase 2: Hybrid Implementation (4-6 weeks)
**Objective:** Build production-ready hybrid system

**Code Changes Required:**

**search_manager.py:**
```python
class HybridSearchManager:
    def __init__(self, es_config, opensearch_config, embedding_model='titan'):
        self.es_manager = ElasticsearchManager(es_config)  # Existing
        self.vector_manager = OpenSearchVectorManager(opensearch_config)  # New
        self.embedding_service = EmbeddingService(embedding_model)

    def search(self, query, mode='hybrid'):
        if mode == 'keyword':
            return self.es_manager.search(query)
        elif mode == 'semantic':
            embedding = self.embedding_service.generate(query)
            return self.vector_manager.similarity_search(embedding)
        else:  # hybrid mode
            keyword_results = self.es_manager.search(query)
            semantic_results = self.vector_manager.similarity_search(
                self.embedding_service.generate(query)
            )
            return self._merge_results(keyword_results, semantic_results)
```

**New Components Needed:**
- `EmbeddingService` - Handles vector generation (Titan/Bedrock integration)
- `OpenSearchVectorManager` - Manages vector index operations
- `ResultMerger` - Combines and re-ranks results from both systems

**Implementation Steps:**
1. Implement embedding generation service
2. Create vector indexing pipeline
3. Build result merging and ranking logic
4. Add search mode selection to API
5. Implement comprehensive logging and monitoring

### Phase 3: Data Migration & Synchronization (3-5 weeks)
**Objective:** Migrate existing data while maintaining sync

**Tasks:**
1. **Full Data Export from Elasticsearch**
   - Use scroll API to export all documents
   - Transform data format for vector storage

2. **Embedding Generation Pipeline**
   - Batch process documents through Titan
   - Store embeddings in S3 tensor indexes
   - Implement error handling and retries

3. **Dual-Write Implementation**
   - Modify all write operations to update both systems
   - Add consistency checks and monitoring
   - Implement conflict resolution logic

4. **Data Validation**
   - Sample-based result comparison
   - Coverage analysis to ensure no data loss
   - Performance testing under load

### Phase 4: User Transition & Testing (3-4 weeks)
**Objective:** Gradual user migration with feedback

**Tasks:**
1. **UI/UX Updates**
   - Add search mode toggle (Keyword/Semantic/Hybrid)
   - Update search help documentation
   - Add feedback mechanism for result relevance

2. **A/B Testing Setup**
   - Randomly assign users to different search modes
   - Track engagement and success metrics
   - Collect qualitative feedback

3. **Performance Optimization**
   - Cache frequent embeddings
   - Optimize query execution plans
   - Tune OpenSearch index configurations

4. **User Training**
   - Create video tutorials on semantic search
   - Update API documentation
   - Conduct live training sessions

### Phase 5: Full Migration Decision (2 weeks)
**Objective:** Evaluate and decide on full migration

**Decision Criteria:**
1. **Performance Metrics**
   - Semantic search relevance > 85% of keyword search
   - Latency < 500ms for 95% of queries
   - Cost increase < 30% from current

2. **User Feedback**
   - >70% positive feedback on semantic results
   - <10% requests to revert to keyword search
   - No critical workflow disruptions

3. **Business Impact**
   - Measurable improvement in key workflows
   - Alignment with long-term AI/ML strategy
   - Justifiable ROI based on productivity gains

**Possible Outcomes:**
- **Proceed with full migration** - Deprecate Elasticsearch
- **Continue hybrid approach** - Maintain both systems
- **Revert to Elasticsearch** - If semantic search fails to meet needs

### Phase 6: Full Migration (Optional, 4-6 weeks)
**Objective:** Complete transition to S3 tensor indexes

**Tasks:**
1. **Final Data Migration**
   - Complete any remaining data transfer
   - Verify 100% data coverage

2. **Elasticsearch Deprecation**
   - Remove dual-write logic
   - Update all read operations to use vector search
   - Monitor for any regressions

3. **Infrastructure Cleanup**
   - Shutdown Elasticsearch clusters
   - Update monitoring and alerting
   - Archive old data as needed

4. **Post-Migration Support**
   - Enhanced user support for transition period
   - Continuous performance monitoring
   - Regular model updates and improvements

## Recommended Tools & Services

**Embedding Generation:**
- Amazon Titan Text v2 (recommended for ease of integration)
- Hugging Face on SageMaker (if customization needed)

**Vector Search:**
- Amazon OpenSearch Serverless with vector engine
- S3 tensor indexes for storage

**Monitoring:**
- Amazon CloudWatch for performance metrics
- OpenSearch Dashboards for search analytics
- AWS X-Ray for tracing search requests

## Risk Mitigation Strategies

1. **Fallback Mechanism** - Maintain Elasticsearch in read-only mode for 3 months post-migration
2. **Feature Flags** - Allow quick rollback of semantic search features
3. **Performance Buffer** - Allocate 2x expected resources during transition
4. **User Segmentation** - Roll out changes to power users first
5. **Comprehensive Testing** - Automated regression tests for search relevance

## Estimated Timeline & Resources

| Phase | Duration | Team | Key Resources |
|-------|----------|------|---------------|
| Decision & Prep | 2-3 weeks | PM, Architects | Analysis documents, stakeholder meetings |
| PoC | 3-4 weeks | 2 Devs, 1 ML Engineer | AWS credits, sample dataset |
| Hybrid Implementation | 4-6 weeks | 3 Devs, 1 QA | Dev/test environments |
| Data Migration | 3-5 weeks | 2 Devs, 1 Data Engineer | ETL pipelines, monitoring |
| User Transition | 3-4 weeks | Full team | UX designer, technical writer |
| Decision Point | 2 weeks | Leadership | Metrics dashboard, user feedback |
| Full Migration | 4-6 weeks | 2 Devs, 1 DevOps | Production environment |

## Recommendation

Given the current simple keyword search implementation and the fundamental paradigm shift required for semantic search, I recommend:

1. **Start with the hybrid approach** as outlined in Phases 1-4
2. **Focus initial efforts on specific use cases** where semantic search provides clear benefits
3. **Maintain Elasticsearch as primary** until semantic search proves superior
4. **Only proceed with full migration** if clear advantages are demonstrated

This approach minimizes risk while allowing you to evaluate the benefits of AWS S3 tensor indexes in a real-world context. The hybrid system can continue indefinitely if it provides the best balance of features and performance.

Would you like me to elaborate on any specific aspect of this plan or provide more detailed technical implementation guidance for particular components?

---

## User

yes, let's elaborate on the steps required to implement the new semantic search features using Titan and Amazon OpenSearch Serverless

---

## Assistant (Plan · devstral-2:123b-cloud · 74.9s)

Let me elaborate on the specific steps required to implement semantic search features using Titan and Amazon OpenSearch Serverless:

## Detailed Implementation Plan for Semantic Search with Titan & OpenSearch Serverless

### Step 1: Set Up AWS Infrastructure (1-2 days)

**Tasks:**
1. **Create OpenSearch Serverless Collection**
   ```bash
   # Using AWS CLI
   aws opensearchserverless create-collection \
     --name "toshi-semantic-search" \
     --type "VECTORSEARCH" \
     --description "Semantic search collection for Toshi API"
   ```

2. **Configure Security Policy**
   - Create data access policy allowing your application role
   - Set up network policy for VPC access if needed
   - Configure encryption policy for data at rest

3. **Set Up S3 Bucket for Tensor Indexes**
   - Create dedicated S3 bucket with proper lifecycle policies
   - Configure bucket policies for OpenSearch access
   - Set up CloudWatch monitoring

### Step 2: Implement Embedding Service (3-5 days)

**New Component: `embedding_service.py`**

```python
import boto3
import json
from typing import List, Dict, Any

class TitanEmbeddingService:
    def __init__(self, model_id="amazon.titan-embed-text-v2:0", region="us-west-2"):
        self.bedrock = boto3.client(
            service_name='bedrock-runtime',
            region_name=region
        )
        self.model_id = model_id
        self.max_tokens = 8192  # Titan v2 limit

    def generate_embedding(self, text: str) -> List[float]:
        """Generate vector embedding for given text using Amazon Titan"""
        if len(text.split()) > self.max_tokens:
            raise ValueError(f"Text exceeds maximum token limit of {self.max_tokens}")

        try:
            response = self.bedrock.invoke_model(
                modelId=self.model_id,
                body=json.dumps({"inputText": text})
            )
            return json.loads(response['body'].read().decode('utf-8'))['embedding']
        except Exception as e:
            # Fallback handling
            raise EmbeddingGenerationError(f"Titan embedding failed: {str(e)}")

    def batch_generate(self, texts: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple texts"""
        return [self.generate_embedding(text) for text in texts]
```

**Key Implementation Details:**
- Error handling for rate limits and service issues
- Text preprocessing (cleanup, normalization)
- Caching mechanism for frequent queries
- Monitoring for embedding generation metrics

### Step 3: Create OpenSearch Vector Manager (5-7 days)

**New Component: `opensearch_vector_manager.py`**

```python
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

class OpenSearchVectorManager:
    def __init__(self, collection_endpoint, index_name="toshi-vectors"):
        credentials = boto3.Session().get_credentials()
        self.awsauth = AWS4Auth(
            credentials.access_key,
            credentials.secret_key,
            region,
            'aoss',
            session_token=credentials.token
        )

        self.client = OpenSearch(
            hosts=[collection_endpoint],
            http_auth=self.awsauth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )

        self.index_name = index_name
        self._ensure_index_exists()

    def _ensure_index_exists(self):
        """Create index with proper vector mapping if it doesn't exist"""
        index_body = {
            "settings": {
                "index.knn": True,
                "index.knn.algo_param.ef_search": 512
            },
            "mappings": {
                "properties": {
                    "vector_field": {
                        "type": "knn_vector",
                        "dimension": 1024,  # Titan v2 dimension
                        "method": {
                            "name": "hnsw",
                            "space_type": "cosinesimil",
                            "engine": "faiss",
                            "parameters": {
                                "ef_construction": 128,
                                "m": 16
                            }
                        }
                    },
                    "metadata": {"type": "object"},
                    "original_id": {"type": "keyword"},
                    "document_type": {"type": "keyword"}
                }
            }
        }

        if not self.client.indices.exists(index=self.index_name):
            self.client.indices.create(index=self.index_name, body=index_body)

    def index_vector(self, document_id: str, vector: List[float], metadata: Dict, doc_type: str):
        """Index a document with its vector embedding"""
        doc = {
            "vector_field": vector,
            "metadata": metadata,
            "original_id": document_id,
            "document_type": doc_type
        }
        return self.client.index(
            index=self.index_name,
            id=document_id,
            body=doc
        )

    def similarity_search(self, query_vector: List[float], k=10, filters=None):
        """Perform k-NN search on vector index"""
        knn = {
            "field": "vector_field",
            "query_vector": query_vector,
            "k": k,
            "num_candidates": 10000
        }

        if filters:
            knn["filter"] = filters

        return self.client.search(
            index=self.index_name,
            body={
                "size": k,
                "query": {"knn": knn},
                "_source": {"excludes": ["vector_field"]}
            }
        )
```

### Step 4: Modify Search Manager (7-10 days)

**Updated `search_manager.py` with Hybrid Support:**

```python
class HybridSearchManager:
    def __init__(self, es_config, opensearch_config):
        # Initialize both search backends
        self.es_manager = ElasticsearchManager(es_config)  # Existing
        self.vector_manager = OpenSearchVectorManager(opensearch_config)
        self.embedding_service = TitanEmbeddingService()

        # Configuration
        self.default_mode = "hybrid"
        self.semantic_weight = 0.7  # Weight for semantic results in hybrid mode
        self.keyword_weight = 0.3   # Weight for keyword results

    def search(self, query: str, mode: str = None, filters: Dict = None):
        mode = mode or self.default_mode

        if mode == "keyword":
            return self._keyword_search(query, filters)
        elif mode == "semantic":
            return self._semantic_search(query, filters)
        else:  # hybrid
            return self._hybrid_search(query, filters)

    def _keyword_search(self, query: str, filters: Dict = None):
        """Original Elasticsearch keyword search"""
        return self.es_manager.search(query)

    def _semantic_search(self, query: str, filters: Dict = None):
        """Pure vector similarity search"""
        try:
            query_vector = self.embedding_service.generate_embedding(query)
            results = self.vector_manager.similarity_search(query_vector, filters=filters)

            # Convert OpenSearch results to consistent format
            return [{
                "id": hit["_source"]["original_id"],
                "score": hit["_score"],
                "type": hit["_source"]["document_type"],
                "metadata": hit["_source"]["metadata"],
                "source": "semantic"
            } for hit in results["hits"]["hits"]]

        except Exception as e:
            # Fallback to keyword search if semantic fails
            return self._keyword_search(query, filters)

    def _hybrid_search(self, query: str, filters: Dict = None):
        """Combine results from both search methods"""
        keyword_results = self._keyword_search(query, filters)
        semantic_results = self._semantic_search(query, filters)

        # Normalize scores and combine
        combined = self._merge_and_rerank(keyword_results, semantic_results)
        return combined

    def _merge_and_rerank(self, keyword_results: List, semantic_results: List) -> List:
        """Merge and rerank results using weighted scoring"""
        # Normalize scores to 0-1 range
        keyword_results = self._normalize_scores(keyword_results, "keyword")
        semantic_results = self._normalize_scores(semantic_results, "semantic")

        # Create unified result set with combined scores
        all_results = {}
        for result in keyword_results + semantic_results:
            doc_id = result["id"]
            if doc_id not in all_results:
                all_results[doc_id] = {
                    "id": doc_id,
                    "type": result["type"],
                    "metadata": result["metadata"],
                    "scores": {"keyword": 0, "semantic": 0},
                    "sources": set()
                }
            all_results[doc_id]["scores"][result["source"]] = result["score"]
            all_results[doc_id]["sources"].add(result["source"])

        # Calculate combined scores and sort
        scored_results = []
        for doc_id, result in all_results.items():
            # Apply weights based on source combination
            if len(result["sources"]) == 2:  # Appears in both
                combined_score = (result["scores"]["keyword"] * self.keyword_weight +
                                result["scores"]["semantic"] * self.semantic_weight)
            else:  # Only in one source
                source = next(iter(result["sources"]))
                combined_score = result["scores"][source]

            scored_results.append({
                **result,
                "combined_score": combined_score,
                "sources": list(result["sources"])
            })

        # Sort by combined score
        return sorted(scored_results, key=lambda x: x["combined_score"], reverse=True)

    def _normalize_scores(self, results: List, source: str) -> List:
        """Normalize scores to 0-1 range for fair comparison"""
        if not results:
            return results

        scores = [r["score"] for r in results]
        min_score, max_score = min(scores), max(scores)

        # Avoid division by zero
        if min_score == max_score:
            normalized = [{"score": 0.5, **r} for r in results]
        else:
            normalized = []
            for r in results:
                normalized_score = (r["score"] - min_score) / (max_score - min_score)
                normalized.append({"score": normalized_score, **r})

        return normalized
```

### Step 5: Implement Data Migration Pipeline (5-7 days)

**Migration Script: `es_to_opensearch_migrator.py`**

```python
class DataMigrator:
    def __init__(self, es_manager, vector_manager, embedding_service, batch_size=100):
        self.es = es_manager
        self.vector = vector_manager
        self.embedding = embedding_service
        self.batch_size = batch_size

    def migrate_all(self):
        """Migrate all documents from Elasticsearch to OpenSearch"""
        # Use scroll API to get all documents
        scroll = self.es.client.scroll(
            index=self.es._es_index,
            scroll='2m',
            size=self.batch_size
        )

        scroll_id = scroll['_scroll_id']
        hits = scroll['hits']['hits']
        total = 0

        while hits:
            batch = []
            for hit in hits:
                doc_id = hit['_id']
                source = hit['_source']

                # Extract relevant metadata
                metadata = {
                    "file_name": source.get("file_name"),
                    "created": source.get("created"),
                    "updated": source.get("updated"),
                    "clazz_name": source.get("clazz_name")
                }

                # Generate text for embedding (customize based on your data)
                text_for_embedding = self._create_embedding_text(source)

                batch.append({
                    "id": doc_id,
                    "text": text_for_embedding,
                    "metadata": metadata,
                    "type": source["clazz_name"]
                })

            # Process batch
            self._process_batch(batch)
            total += len(batch)

            # Get next batch
            scroll = self.es.client.scroll(
                scroll_id=scroll_id,
                scroll='2m'
            )
            scroll_id = scroll['_scroll_id']
            hits = scroll['hits']['hits']

        return total

    def _create_embedding_text(self, document: Dict) -> str:
        """Create text representation for embedding generation"""
        # Customize based on your document types
        if document['clazz_name'] == 'File':
            return f"File: {document.get('file_name', '')}. {document.get('description', '')}"
        elif document['clazz_name'] == 'Thing':
            return f"Thing: {document.get('name', '')}. {document.get('description', '')}"
        else:
            return json.dumps(document)

    def _process_batch(self, batch: List[Dict]):
        """Generate embeddings and index batch"""
        try:
            # Generate embeddings for batch
            texts = [item['text'] for item in batch]
            embeddings = self.embedding.batch_generate(texts)

            # Index documents with embeddings
            for item, embedding in zip(batch, embeddings):
                self.vector.index_vector(
                    document_id=item['id'],
                    vector=embedding,
                    metadata=item['metadata'],
                    doc_type=item['type']
                )

        except Exception as e:
            # Log error and continue with next batch
            log.error(f"Batch processing failed: {str(e)}")
            raise
```

### Step 6: Update API and GraphQL Schema (3-5 days)

**GraphQL Schema Updates:**

```graphql
type Query {
    search(
        searchTerm: String!
        searchMode: SearchMode = HYBRID
        filters: SearchFilters
        limit: Int = 20
    ): SearchResult!
}

enum SearchMode {
    KEYWORD
    SEMANTIC
    HYBRID
}

input SearchFilters {
    documentTypes: [String]
    dateRange: DateRange
    # Add other relevant filters
}

type SearchResult {
    totalCount: Int!
    results: [SearchResultItem]!
    searchMode: SearchMode!
    timing: SearchTiming
}

type SearchResultItem {
    id: ID!
    type: String!
    score: Float!
    metadata: JSON!
    sources: [String!]!  # Which search methods found this result
}

type SearchTiming {
    total: Float!
    keywordSearch: Float
    semanticSearch: Float
    merging: Float
}
```

**Resolver Implementation:**

```python
class SearchQuery(graphene.ObjectType):
    search = graphene.Field(
        SearchResult,
        search_term=graphene.String(required=True),
        search_mode=graphene.Argument(SearchMode, default_value="HYBRID"),
        filters=graphene.Argument(SearchFilters),
        limit=graphene.Int(default_value=20)
    )

    def resolve_search(self, info, search_term, search_mode, filters=None, limit=20):
        search_manager = info.context['search_manager']

        # Convert filters to backend format
        backend_filters = self._convert_filters(filters) if filters else None

        # Perform search
        start_time = time.time()
        results = search_manager.search(
            query=search_term,
            mode=search_mode.value.lower(),
            filters=backend_filters
        )

        # Format results
        formatted_results = []
        for result in results[:limit]:
            formatted_results.append({
                "id": result["id"],
                "type": result["type"],
                "score": result["combined_score"] if "combined_score" in result else result["score"],
                "metadata": result["metadata"],
                "sources": result.get("sources", [search_mode.value.lower()])
            })

        return {
            "totalCount": len(results),
            "results": formatted_results,
            "searchMode": search_mode,
            "timing": {
                "total": time.time() - start_time,
                # Additional timing metrics would be captured in search_manager
            }
        }
```

### Step 7: Implement Monitoring and Analytics (3-5 days)

**CloudWatch Dashboard Setup:**
1. **Search Performance Metrics:**
   - Latency by search mode (keyword vs semantic vs hybrid)
   - Throughput (requests per second)
   - Error rates and types

2. **Relevance Tracking:**
   - Click-through rates by result position
   - User feedback scores
   - Result diversity metrics

3. **Cost Monitoring:**
   - Titan embedding generation costs
   - OpenSearch compute unit usage
   - S3 storage costs

**Sample Monitoring Code:**

```python
class SearchMonitor:
    def __init__(self):
        self.cloudwatch = boto3.client('cloudwatch')
        self.namespace = "Toshi/Search"

    def track_search(self, search_mode: str, duration: float, result_count: int, has_error: bool = False):
        """Track search operation metrics"""
        metrics = [
            {
                'MetricName': 'SearchLatency',
                'Dimensions': [{'Name': 'SearchMode', 'Value': search_mode}],
                'Value': duration,
                'Unit': 'Milliseconds'
            },
            {
                'MetricName': 'ResultCount',
                'Dimensions': [{'Name': 'SearchMode', 'Value': search_mode}],
                'Value': result_count,
                'Unit': 'Count'
            },
            {
                'MetricName': 'SearchCount',
                'Dimensions': [{'Name': 'SearchMode', 'Value': search_mode}],
                'Value': 1,
                'Unit': 'Count'
            }
        ]

        if has_error:
            metrics.append({
                'MetricName': 'ErrorCount',
                'Dimensions': [{'Name': 'SearchMode', 'Value': search_mode}],
                'Value': 1,
                'Unit': 'Count'
            })

        self.cloudwatch.put_metric_data(
            Namespace=self.namespace,
            MetricData=metrics
        )

    def track_relevance(self, search_mode: str, result_position: int, is_clicked: bool):
        """Track result relevance metrics"""
        self.cloudwatch.put_metric_data(
            Namespace=self.namespace,
            MetricData=[{
                'MetricName': 'ClickThroughRate',
                'Dimensions': [
                    {'Name': 'SearchMode', 'Value': search_mode},
                    {'Name': 'Position', 'Value': str(result_position)}
                ],
                'Value': 1 if is_clicked else 0,
                'Unit': 'Count'
            }]
        )
```

### Step 8: Testing and Validation (2-3 weeks)

**Test Plan:**

1. **Unit Testing:**
   - Embedding generation consistency
   - Vector indexing and retrieval
   - Score normalization and merging logic
   - Error handling and fallbacks

2. **Integration Testing:**
   - End-to-end search workflows
   - Hybrid search result merging
   - Filter application correctness
   - Performance under load

3. **User Acceptance Testing:**
   - Side-by-side comparison with existing search
   - Relevance scoring by domain experts
   - Workflow integration testing

4. **Performance Testing:**
   - Load testing with production-like data volumes
   - Latency benchmarks
   - Failure recovery testing

**Sample Test Cases:**

```python
class TestSemanticSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Initialize test infrastructure
        cls.embedding_service = TitanEmbeddingService()
        cls.vector_manager = OpenSearchVectorManager(test_index="test-vectors")
        cls.search_manager = HybridSearchManager(es_config, opensearch_config)

        # Index test data
        cls._index_test_data()

    @classmethod
    def _index_test_data(cls):
        """Index sample documents for testing"""
        test_docs = [
            {
                "id": "file-1",
                "type": "File",
                "text": "Seismic hazard analysis report for Wellington region",
                "metadata": {"file_name": "wellington_hazard.pdf"}
            },
            {
                "id": "file-2",
                "type": "File",
                "text": "Ground motion prediction equations for New Zealand",
                "metadata": {"file_name": "gmpe_nz.pdf"}
            }
        ]

        for doc in test_docs:
            vector = cls.embedding_service.generate_embedding(doc["text"])
            cls.vector_manager.index_vector(
                document_id=doc["id"],
                vector=vector,
                metadata=doc["metadata"],
                doc_type=doc["type"]
            )

    def test_embedding_generation(self):
        """Test that embeddings are generated consistently"""
        text = "Test document content"
        embedding1 = self.embedding_service.generate_embedding(text)
        embedding2 = self.embedding_service.generate_embedding(text)

        # Embeddings should be identical for same input
        self.assertEqual(embedding1, embedding2)
        self.assertEqual(len(embedding1), 1024)  # Titan v2 dimension

    def test_vector_search(self):
        """Test basic vector similarity search"""
        query = "hazard analysis for Wellington"
        query_vector = self.embedding_service.generate_embedding(query)

        results = self.vector_manager.similarity_search(query_vector, k=5)

        # Should find our test document
        self.assertGreater(len(results["hits"]["hits"]), 0)
        self.assertEqual(results["hits"]["hits"][0]["_source"]["original_id"], "file-1")

    def test_hybrid_search(self):
        """Test hybrid search combines results properly"""
        results = self.search_manager.search("Wellington hazard", mode="hybrid")

        # Should have results from both sources
        self.assertGreater(len(results), 0)
        self.assertIn("sources", results[0])
        self.assertIn(results[0]["sources"], ["keyword", "semantic"])

    def test_fallback_behavior(self):
        """Test that system falls back to keyword search on semantic failure"""
        # Mock embedding service to fail
        with patch.object(self.embedding_service, 'generate_embedding', side_effect=Exception("Service error")):
            results = self.search_manager.search("test query", mode="semantic")

            # Should still return results (from keyword search)
            self.assertGreater(len(results), 0)
```

### Step 9: Deployment Strategy (1 week)

**Phased Rollout Plan:**

1. **Blue/Green Deployment:**
   - Deploy new search service alongside existing
   - Route small percentage of traffic to new service
   - Monitor for errors and performance issues

2. **Canary Testing:**
   - Select group of power users for initial testing
   - Collect detailed feedback and metrics
   - Iterate based on findings

3. **Gradual Ramp-Up:**
   - Increase traffic to new service in 10% increments
   - Monitor key metrics at each stage
   - Implement circuit breakers for automatic rollback

4. **Full Cutover:**
   - Once metrics meet success criteria
   - With comprehensive rollback plan in place
   - During low-traffic period

### Step 10: Post-Deployment Optimization (Ongoing)

**Continuous Improvement Activities:**

1. **Embedding Model Tuning:**
   - Experiment with different Titan model versions
   - Consider fine-tuning if needed
   - Monitor for new model releases

2. **Search Relevance Optimization:**
   - Adjust scoring weights based on user feedback
   - Implement query expansion techniques
   - Add synonym handling

3. **Performance Optimization:**
   - Cache frequent queries and embeddings
   - Optimize OpenSearch index settings
   - Right-size compute resources

4. **User Education:**
   - Create best practices guides
   - Conduct training sessions
   - Gather continuous feedback

## Implementation Checklist

- [ ] Set up AWS infrastructure (OpenSearch, Bedrock, S3)
- [ ] Implement embedding service with error handling
- [ ] Create vector manager with proper index mappings
- [ ] Update search manager with hybrid logic
- [ ] Build data migration pipeline
- [ ] Update GraphQL schema and resolvers
- [ ] Implement comprehensive monitoring
- [ ] Write test suite (unit, integration, performance)
- [ ] Create deployment pipeline
- [ ] Develop user documentation and training

## Key Considerations

1. **Cost Management:**
   - Monitor Titan embedding costs closely
   - Implement caching for frequent queries
   - Set up budget alerts

2. **Performance:**
   - Vector search has ~60s refresh interval vs Elasticsearch
   - Plan for higher latency in semantic searches
   - Consider pre-computing embeddings for static content

3. **User Experience:**
   - Provide clear search mode selection
   - Offer examples of effective semantic queries
   - Include feedback mechanism for relevance tuning

4. **Operational:**
   - Implement proper logging and error tracking
   - Set up alerts for service degradation
   - Document runbooks for common issues

This implementation plan provides a comprehensive approach to adding semantic search capabilities using Amazon Titan and OpenSearch Serverless while maintaining backward compatibility with the existing Elasticsearch implementation. The hybrid approach minimizes risk and allows for gradual adoption based on real-world performance and user feedback.

---

