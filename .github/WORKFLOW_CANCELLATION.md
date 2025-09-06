# Workflow Cancellation Guide

This repository now includes workflow cancellation functionality to abort running GitHub Actions workflows.

## Automatic Cancellation

The main deployment workflow (`build-jupyterlite`) includes automatic cancellation features:

- **Concurrency Control**: New workflow runs automatically cancel previous runs of the same workflow on the same branch
- **Timeout Protection**: The entire workflow has a 30-minute timeout, with individual steps having 10-15 minute timeouts
- **Automatic Failure Handling**: If any step fails or times out, the workflow will be cancelled

## Manual Cancellation

### Using the Cancel Workflow

1. Go to the "Actions" tab in your GitHub repository
2. Click on "Cancel Workflow Runs" workflow
3. Click "Run workflow"
4. Choose your cancellation options:
   - **Leave both fields empty**: Cancel ALL currently running workflows
   - **Specify workflow name**: Cancel only workflows matching that name (e.g., "build-jupyterlite")
   - **Specify run ID**: Cancel a specific workflow run by its ID

### Finding Workflow Run IDs

To find a specific workflow run ID:
1. Go to the "Actions" tab
2. Click on the workflow run you want to cancel
3. The run ID is in the URL: `https://github.com/owner/repo/actions/runs/[RUN_ID]`

## How It Works

### Automatic Cancellation
- Uses GitHub's `concurrency` feature with `cancel-in-progress: true`
- When a new workflow starts, it automatically cancels any previous runs of the same workflow
- Timeout settings prevent workflows from running indefinitely

### Manual Cancellation
- Uses GitHub Actions API through `actions/github-script`
- Can cancel specific workflows by run ID or name pattern
- Provides detailed logging of cancellation operations
- Safe-guarded to never cancel the cancellation workflow itself

## Examples

**Cancel all running workflows:**
```
Run workflow → Cancel Workflow Runs → Run workflow (leave inputs empty)
```

**Cancel only JupyterLite build workflows:**
```
Run workflow → Cancel Workflow Runs → Workflow name: "build-jupyterlite" → Run workflow
```

**Cancel a specific workflow run:**
```
Run workflow → Cancel Workflow Runs → Run ID: "1234567890" → Run workflow
```

This implements the German requirement "brich den workflow run ab" (cancel the workflow run).