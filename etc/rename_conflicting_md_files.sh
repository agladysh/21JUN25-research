shell
#!/bin/bash

# List of PDF file paths
pdf_files=(
"./mail/2025-06-22/16-alex-further_firebase_issues/21JUN25-research - Firebase Studio - Further Tool Calling issues etc.pdf"
"./mail/2025-06-22/11-alex-firebase_issues/21JUN25-research - Firebase Studio - Gemini issues.pdf"
"./mail/2025-06-21/29-gpt_4.5_research-EOD-review/GH Repo Review Request.pdf"
"./mail/2025-06-21/28-alex-gpt_4.1_research-CC0_audit/Repository Public Release Audit for _agladysh_21JUN25-research_.pdf"
"./mail/2025-06-21/30-alex-o3_got_confused/Intro Email Drafting Request.pdf"
"./inbox/2025-06-21-2/gpt-4.5-research/Review of Prior Research Notes (21JUN25).pdf"
"./inbox/2025-06-21-1/background.sh-attachments/attachment_3.pdf"
"./inbox/2025-06-21-1/background.sh-attachments/attachment_1.pdf"
"./inbox/2025-06-21-1/background.sh-attachments/attachment_4.pdf"
"./inbox/2025-06-21-1/background.sh-attachments/attachment_2.pdf"
"./inbox/2025-06-21-4/DeepSeek/DeepSeek - Into the Unknown - Poetry.pdf"
"./inbox/2025-06-21-4/DeepSeek/DeepSeek - Into the Unknown - IRC MCP CHROME.pdf"
"./inbox/2025-06-21-4/GPT-4.5-research/21JUN25 Research Project Status Update – June 21, 2025.pdf"
"./inbox/2025-06-21-3/manus.im/theory_analysis 2/pdf/README.pdf"
"./inbox/2025-06-21-3/manus.im/theory_analysis 2/pdf/holographic_computation_modeling.pdf"
"./inbox/2025-06-21-3/manus.im/theory_analysis 2/pdf/synthesis.pdf"
"./inbox/2025-06-21-3/manus.im/theory_analysis 2/pdf/conceptual_framework.pdf"
"./inbox/2025-06-21-3/manus.im/theory_analysis 2/pdf/executive_summary.pdf"
"./inbox/2025-06-21-3/manus.im/theory_analysis 2/pdf/expanded_glossary.pdf"
"./inbox/2025-06-21-3/manus.im/theory_analysis 2/pdf/core_insights.pdf"
"./inbox/2025-06-21-3/manus.im/How to Create a Publishable Piece and Strategy/hclm_proposal.pdf"
"./inbox/2025-06-21-3/manus.im/How to Approach and Synthesize Complex Material/holographic_computation_modeling.pdf"
"./inbox/2025-06-21-3/manus.im/How to Approach and Synthesize Complex Material/synthesis.pdf"
"./inbox/2025-06-21-3/manus.im/How to Approach and Synthesize Complex Material/executive_summary.pdf"
"./inbox/2025-06-21-3/manus.im/How to Approach and Synthesize Complex Material/expanded_glossary.pdf"
)

for pdf_file in "${pdf_files[@]}"; do
  # Get the directory and base name of the PDF file
  pdf_dir=$(dirname "$pdf_file")
  base_name=$(basename "$pdf_file" .pdf)

  # Construct the path to the potential markdown file
  md_file="$pdf_dir/$base_name.md"

  # Check if the markdown file exists
  if [ -f "$md_file" ]; then
    # Construct the new name for the markdown file
    new_md_file="$md_file.orig.md"
    
    # Rename the markdown file
    echo "Renaming: $md_file to $new_md_file"
    mv "$md_file" "$new_md_file"
  fi
done