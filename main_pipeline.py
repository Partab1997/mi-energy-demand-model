import warnings

# Parameter boundaries
bounds = []

# alpha
for _ in range(7):
    bounds.append((-1, 0))

# delta
for _ in range(12):
    bounds.append((0, 1))

bounds.append((0, 1))

# rho
bounds.append((-1, 1))

result = differential_evolution(
    objective,
    bounds,
    maxiter=40,
    popsize=10,
    tol=0.01,
    polish=True,
    seed=42,
    workers=1
)

print("Optimization completed")
print(result.x)

opt_df = pd.DataFrame({
    "parameter": [f"param_{i}" for i in range(len(result.x))],
    "value": result.x
})

opt_df.to_csv(
    "outputs/tables/optimized_parameters.csv",
    index=False
)

# =========================================================
# SAVE FINAL MODEL RESULTS
# =========================================================

summary_text = f"""
MEE Energy Demand Model Summary
================================

RMSE: {rmse}
MAE: {mae}
R2: {r2}

Optimization Objective: {result.fun}

"""

with open("outputs/model_summary.txt", "w") as f:
    f.write(summary_text)

print(summary_text)

print("Pipeline completed successfully.")
