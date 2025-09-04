# Error Metrics in Predictive Models

When evaluating predictive models, it’s essential to quantify how far off the predictions are from actual values. Common metrics include **MSE**, **RMSE**, **MAE**, and **MAPE**.

---

## 1. Mean Squared Error (MSE)

MSE measures the average of the squared differences between predicted and actual values.

<!-- prettier-ignore -->
\[
\text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2
\]

<!-- prettier-ignore -->
- \(y_i\) = actual value
- \(\hat{y}_i\) = predicted value
- \(n\) = number of observations

**Key Characteristics:**

- Penalises larger errors more than smaller ones (due to squaring).
- Useful when large deviations are particularly undesirable.

**Example:**

<!-- prettier-ignore -->
| Actual (\(y_i\)) | Predicted (\(\hat{y}_i\)) |
| ---------------- | -------------------------- |
| 10               | 12                         |
| 15               | 14                         |
| 20               | 17                         |

\[
\text{MSE} = \frac{(10-12)^2 + (15-14)^2 + (20-17)^2}{3} = \frac{4 + 1 + 9}{3} = 4.67
\]

---

## 2. Root Mean Squared Error (RMSE)

RMSE is simply the square root of MSE, bringing the error back to the original unit of measurement.

\[
\text{RMSE} = \sqrt{\text{MSE}}
\]

**Key Characteristics:**

- Easier to interpret than MSE because it’s in the same units as the original data.
- Still penalises large deviations strongly.

**Example:**

Using the MSE above:

\[
\text{RMSE} = \sqrt{4.67} \approx 2.16
\]

---

## 3. Mean Absolute Error (MAE)

MAE measures the average of the absolute differences between predicted and actual values.

<!-- prettier-ignore -->
\[
\text{MAE} = \frac{1}{n} \sum_{i=1}^{n} \left|y_i - \hat{y}_i\right|
\]

**Key Characteristics:**

- Treats all errors equally (no squaring).
- More robust to outliers compared to MSE/RMSE.

**Example:**

\[
\text{MAE} = \frac{|10-12| + |15-14| + |20-17|}{3} = \frac{2 + 1 + 3}{3} = 2.0
\]

---

## 4. Mean Absolute Percentage Error (MAPE)

MAPE expresses the error as a percentage of the actual value.

<!-- prettier-ignore -->
\[
\text{MAPE} = \frac{100\%}{n} \sum_{i=1}^{n} \left| \frac{y_i - \hat{y}_i}{y_i} \right|
\]

**Key Characteristics:**

- Provides an intuitive “percentage error”.
- Not suitable when actual values (\(y_i\)) can be zero (division by zero problem).

**Example:**

\[
\text{MAPE} = \frac{100}{3} \left(
\left|\frac{10-12}{10}\right| +
\left|\frac{15-14}{15}\right| +
\left|\frac{20-17}{20}\right|
\right)
\]

\[
= \frac{100}{3} (0.20 + 0.0667 + 0.15) \approx 13.9\%
\]

---

## Summary Table

| Metric   | Formula                                                        | Penalises Outliers? | Units          |
| -------- | -------------------------------------------------------------- | ------------------- | -------------- |
| **MSE**  | \(\frac{1}{n}\sum (y-\hat{y})^2\)                              | Strongly            | Squared units  |
| **RMSE** | \(\sqrt{\text{MSE}}\)                                          | Strongly            | Original units |
| **MAE**  | \(\frac{1}{n}\sum \vert y-\hat{y}\vert\)                       | Mildly              | Original units |
| **MAPE** | \(\frac{100}{n}\sum \left\vert\frac{y-\hat{y}}{y}\right\vert\) | Mildly              | Percentage     |
