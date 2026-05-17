# ml-service/jurisdiction_config.py

JURISDICTION = {
    "code": "GB",
    "name": "United Kingdom",
    "currency_symbol": "£",
    "currency_code": "GBP",
    "financial_intelligence_unit": "NCA",
    "primary_aml_law": "Proceeds of Crime Act 2002 (POCA)",
    "kyc_framework": "FCA MLR 2017",
    "sar_deadline_days": 7,  # Aligns with statutory NCA DAML notice period
    "sar_report_name": "Suspicious Activity Report",

    "typology_references": {
        "structuring": {
            "fatf_ref": "FATF Recommendation 20",  # CORRECTED: Mandates Suspicious Transaction Reporting
            "local_ref": "POCA 2002 Section 327",
            "description": "Transaction volume or amounts manipulated to evade standard detection thresholds"
        },
        "unusual_timing": {
            "fatf_ref": "FATF Recommendation 10",
            "local_ref": "FCA MLR 2017 Regulation 28",
            "description": "Transaction executed at an anomalous hour inconsistent with user profile"
        },
        "high_risk_merchant": {
            "fatf_ref": "FATF Recommendation 10",
            "local_ref": "FCA MLR 2017 Regulation 33",
            "description": "High-velocity or large-ticket routing to a high-risk merchant category"
        },
        "network_risk": {
            "fatf_ref": "FATF Recommendation 20",  # CORRECTED: Mandates reporting of suspicious entity networks
            "local_ref": "POCA 2002 Section 330",
            "description": "Entity structurally connected via graph network to known or heavily flagged fraud rings"
        }
    }
}

# ==============================================================================
# JURISDICTION SWAP EXAMPLES (Keep these as comments for interview reference)
# ==============================================================================
# IN example:
# "code": "IN", "currency_symbol": "₹", "currency_code": "INR",
# "financial_intelligence_unit": "FIU-IND",
# "primary_aml_law": "PMLA 2002", "kyc_framework": "RBI Master Direction KYC 2016",
# "sar_deadline_days": 7, "sar_report_name": "Suspicious Transaction Report"
#
# US example:
# "code": "US", "currency_symbol": "$", "currency_code": "USD",
# "financial_intelligence_unit": "FinCEN",
# "primary_aml_law": "Bank Secrecy Act (BSA)", "kyc_framework": "FinCEN CDD Rule",
# "sar_deadline_days": 30, "sar_report_name": "Suspicious Activity Report"