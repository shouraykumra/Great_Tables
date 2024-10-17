import pandas as pd

# df = pd.read_csv("/Users/shouraykumra/Downloads/Random_Explanation_of_Benefit_Data.csv")

from great_tables import GT, html, loc, style

claims_df = pd.read_csv("/Users/shouraykumra/Downloads/Random_Explanation_of_Benefit_Data.csv")
rename = {
    'Patient Reference': 'Patient_FHIR_ID',
    'Claim Amount Submitted': 'Claim_Amount_Submitted',
    'Claim Amount Paid to Provider': 'Claim_Amount_Paid_to_Provider',
    'Claim Amount Paid by Patient': 'Claim_Amount_Paid_by_Patient'
}

claims_df.rename(columns=rename, inplace=True)
claims_df.drop(columns=["Diagnosis Code", "Diagnosis Type", "Use", "Type"], inplace=True)
claims_df = claims_df.head(10)
# print(claims_df.columns)
gt_claims = (
    GT(claims_df)
    .tab_header(
        title="Claims Implementation Guide Sample Data",
        subtitle="Explanation of Benefits Institutional Type",

    )
    .tab_spanner(label="Time", columns=["Billable Period Start", "Billable Period End", "Created"])
    .tab_spanner(label="Explanation of Benefit Related Information", columns=["EOB ID", "Patient_FHIR_ID", "Status", "Insurer", "Provider", "SubType"])
    .tab_spanner(label="Results", columns=["Outcome"])
    .tab_spanner(label="Payments", columns=["Claim_Amount_Submitted", "Claim_Amount_Paid_to_Provider", "Claim_Amount_Paid_by_Patient"])
    .cols_move_to_start(columns=["Billable Period Start", "Billable Period End", "Created"])
    .cols_label(
        Patient_FHIR_ID=html("Patient_FHIR_ID,<br>Logical ID"),
        Claim_Amount_Submitted=html("Claim Amount Submitted,<br>$"),
        Claim_Amount_Paid_to_Provider=html("Claim Amount Paid to Provider,<br>$"),
        Claim_Amount_Paid_by_Patient=html("Claim Amount Paid by Patient,<br>$"),
    )
    .fmt_number(
        columns = ["Claim_Amount_Submitted", "Claim_Amount_Paid_to_Provider", "Claim_Amount_Paid_by_Patient"],
        compact=True,
        pattern='${x}',
        n_sigfig=3
    )
    .tab_style(
        locations = loc.body(columns=["Claim_Amount_Submitted", "Claim_Amount_Paid_to_Provider", "Claim_Amount_Paid_by_Patient"]),
        style=style.fill(color='aliceblue')
    )
    .tab_style(
        locations = loc.body(columns=["Billable Period Start", "Billable Period End", "Created"]),
        style=style.fill(color='lightgray')
    )
)

gt_claims
