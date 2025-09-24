
# Project: Visualizing Snowflake RBAC for Enhanced Data Governance

## 1. Introduction

This document outlines the requirements for a web-based tool designed to visualize and analyze Snowflake's Role-Based Access Control (RBAC) structure. The project aims to provide an intuitive and interactive "vibe coding" experience for understanding and managing complex access control policies, thereby improving data governance and compliance.

## 2. Problem Statement

Understanding the intricate web of roles, grants, and privileges in a large Snowflake account is challenging. The lack of a clear, visual representation makes it difficult to audit access, identify potential security risks, and ensure compliance with data governance policies.

## 3. Proposed Solution

A web application that fetches Snowflake RBAC metadata and presents it in a visually engaging and interactive manner. The tool will leverage AI-powered insights to provide actionable recommendations for improving the RBAC configuration.

### 3.1. Core Features

- **RBAC Data Ingestion:**
    - Connect to a Snowflake account using secure credentials.
    - Execute `SHOW` commands (`SHOW GRANTS`, `SHOW ROLES`, etc.) to fetch RBAC metadata.
    - Periodically refresh the data to ensure the visualization is up-to-date.
- **Interactive Graph Visualization:**
    - Represent the RBAC hierarchy (roles, users, and their relationships) as an interactive network graph.
    - Display objects (databases, schemas, tables) and their associated grants.
    - Allow users to click on nodes (roles, users, objects) to view detailed information in a side panel.
- **Filtering and Search:**
    - Filter the visualization by role, user, object type, or privilege.
    - Search for specific roles, users, or objects within the graph.
- **Drill-Down Views:**
    - Provide a tabular view of grants and privileges for a selected role or object.

### 3.2. "Vibe Coding" Elements

- **Color-Coding:**
    - Use distinct colors to represent different role types (e.g., custom roles, system roles).
    - Differentiate between various object types (e.g., tables, views, stages).
    - Highlight different privilege levels (e.g., ownership, read-only, write).
- **Animations and Transitions:**
    - Use smooth animations for graph layout changes and filtering.
    - Implement interactive hover effects to display tooltips with summary information.

### 3.3. AI-Powered Insights

- **Anomaly Detection:**
    - Identify unusual or potentially risky grant configurations (e.g., overly permissive roles, inactive roles with high privileges).
    - Flag users with access to sensitive data that deviates from their typical access patterns.
- **Compliance Checks:**
    - Define and enforce custom compliance policies (e.g., separation of duties).
    - Automatically scan for violations and provide alerts.
- **Optimization Recommendations:**
    - Suggest role consolidation opportunities to simplify the RBAC structure.
    - Recommend the principle of least privilege by identifying and flagging excessive permissions.

## 4. Technical Requirements

- **Frontend:**
    - A web framework like Streamlit, Dash, or a custom React application.
    - A graph visualization library such as D3.js, vis.js, or Cytoscape.js.
- **Backend:**
    - A Python backend (if using Dash or a custom framework) to connect to Snowflake and process data.
    - Use the Snowflake Connector for Python.
- **Deployment:**
    - The application should be deployable as a web service (e.g., using Docker and a cloud platform).

## 5. Non-Functional Requirements

- **Usability:** The interface should be intuitive and require minimal training.
- **Performance:** The graph visualization should render quickly, even for large Snowflake accounts. Data fetching and processing should be optimized.
- **Security:** Snowflake credentials must be stored securely. The application should not store any sensitive data from the Snowflake account.
- **Scalability:** The solution should be able to handle a growing number of roles, users, and objects.

## 6. Success Criteria

- A fully functional web application that meets all the requirements listed above.
- Positive feedback from users on the tool's usability and effectiveness.
- A clear demonstration of how the tool can improve data governance and compliance in a Snowflake environment. 