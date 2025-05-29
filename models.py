def get_recommendations(problem_type, accuracy, explainability, data_size):
    results = []

    if problem_type == "Classification":
        if explainability == "Yes":
            results.append({"model": "Logistic Regression", "reason": "Simple and easy to explain"})
        if accuracy == "Yes":
            results.append({"model": "Random Forest", "reason": "Handles complexity and avoids overfitting"})
        results.append({"model": "XGBoost", "reason": "High performance with larger datasets"})

    elif problem_type == "Regression":
        if explainability == "Yes":
            results.append({"model": "Linear Regression", "reason": "Baseline model with clear interpretation"})
        if accuracy == "Yes":
            results.append({"model": "Gradient Boosting Regressor", "reason": "Good performance on structured data"})

    elif problem_type == "Clustering":
        results.append({"model": "K-Means", "reason": "Fast and easy to implement"})
        if data_size == "Small":
            results.append({"model": "Hierarchical Clustering", "reason": "Good for visualization"})
        if data_size == "Large":
            results.append({"model": "DBSCAN", "reason": "Handles noise and arbitrary shapes"})

    elif problem_type == "Recommendation":
        results.append({"model": "Collaborative Filtering", "reason": "User-item behavior based"})
        results.append({"model": "Content-Based Filtering", "reason": "Uses item metadata for suggestions"})

    return results
