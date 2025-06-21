#!/usr/bin/env python3
import re
import json

def extract_conversations(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Find the JSON block
    start_marker = 'cat << EOF > request.json'
    end_marker = 'EOF'
    
    start_idx = content.find(start_marker)
    if start_idx == -1:
        return "Could not find start marker"
    
    start_idx += len(start_marker)
    end_idx = content.find(end_marker, start_idx)
    if end_idx == -1:
        return "Could not find end marker"
    
    json_str = content[start_idx:end_idx].strip()
    
    # Extract conversation turns
    user_turns = []
    model_turns = []
    
    # Extract user messages
    user_pattern = r'"role": "user",\s*"parts": \[\s*{\s*"text": "(.*?)"\s*},\s*\]'
    user_matches = re.findall(user_pattern, content, re.DOTALL)
    for match in user_matches:
        user_turns.append(match.replace('\\n', '\n'))
    
    # Extract model messages
    model_pattern = r'"role": "model",\s*"parts": \[\s*{\s*"text": "(.*?)"\s*},\s*\]'
    model_matches = re.findall(model_pattern, content, re.DOTALL)
    for match in model_matches:
        model_turns.append(match.replace('\\n', '\n'))
    
    # Combine into conversation
    conversation = []
    for i in range(max(len(user_turns), len(model_turns))):
        if i < len(user_turns):
            conversation.append({"role": "user", "content": user_turns[i]})
        if i < len(model_turns):
            conversation.append({"role": "model", "content": model_turns[i]})
    
    return conversation

if __name__ == "__main__":
    file_path = "/home/ubuntu/upload/theory.sh"
    conversation = extract_conversations(file_path)
    
    # Save to file
    with open("/home/ubuntu/theory_analysis/extracted/conversation.json", "w") as f:
        json.dump(conversation, f, indent=2, ensure_ascii=False)
    
    print(f"Extracted {len(conversation)} conversation turns")
    
    # Also save raw text content
    with open("/home/ubuntu/theory_analysis/extracted/raw_content.txt", "w") as f:
        for turn in conversation:
            f.write(f"--- {turn['role'].upper()} ---\n")
            f.write(turn['content'])
            f.write("\n\n")
    
    print("Content saved to /home/ubuntu/theory_analysis/extracted/")

