Based on my analysis of the project structure and the `serverless.yml` file, here's a document outlining the services and environment variables needed to deploy this project:

# Deployment Documentation for nzshm22-toshi-api

## Services Required

1. **AWS Lambda**: Hosts the GraphQL API
2. **API Gateway**: Provides HTTP endpoints for the GraphQL API
3. **Amazon S3**: For file storage (bucket created automatically)
4. **Amazon Elasticsearch Service**: Version 6.2 for search functionality
5. **Amazon DynamoDB**: For data storage (configured locally for testing)
6. **CloudWatch**: For metrics and logging

## Environment Variables

### Required Environment Variables
These are automatically configured by the Serverless framework but may need to be set in your deployment environment:

- `REGION`: AWS region (default: ap-southeast-2)
- `S3_BUCKET_NAME`: Name of the S3 bucket (auto-generated based on service name and stage)
- `URL_DEFAULT_TTL`: TTL for presigned URLs (default: 60 seconds)
- `DEPLOYMENT_STAGE`: Deployment stage (local, dev, test, prod)
- `ES_ENDPOINT`: Elasticsearch endpoint URL
- `ES_INDEX`: Elasticsearch index name (default: toshi_index_mapped)
- `ES_REGION`: Elasticsearch region
- `ES_DOMAIN_NAME`: Elasticsearch domain name
- `STACK_NAME`: CloudFormation stack name
- `FIRST_DYNAMO_ID`: Starting ID for DynamoDB items (default: 100000)

### Optional Environment Variables (for local development)
- `SLS_OFFLINE`: Set to 1 for local development
- `TESTING`: Set to 1 for testing environment
- `DB_READ_ONLY`: Set to 1 for read-only database access
- `CLOUDWATCH_ENABLED`: Enable CloudWatch metrics (default: yes)
- `MIGRATE_FILE_TO_RUPTSET`: Enable dynamic migrations (default: no)
- `TOSHI_FIX_RANDOM_SEED`: Fix random seed for reproducible tests
- `LOGGING_CFG`: Path to logging configuration file

## Deployment Prerequisites

1. **AWS Credentials**: Configured with appropriate permissions
2. **Serverless Framework**: Installed globally (`npm install -g serverless`)
3. **Python 3.12**: Required runtime
4. **Poetry**: For dependency management
5. **Node.js**: For Serverless plugins (version 22 recommended)
6. **Yarn**: For package management

## Deployment Steps

1. Install dependencies:
   ```bash
   yarn install
   poetry install
   ```

2. Configure AWS credentials in `~/.aws/credentials`

3. Deploy the stack:
   ```bash
   serverless deploy --stage [stage-name]
   ```

4. For local development:
   ```bash
   yarn sls dynamodb start --stage local
   yarn sls s3 start
   docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.8.0
   poetry run yarn sls wsgi serve
   ```

## Notes

- The project uses Elasticsearch 6.2, which is an older version
- DynamoDB is configured for local in-memory testing by default
- The API requires an API key for production deployments
- Lambda function has 8GB memory and 30-second timeout configured