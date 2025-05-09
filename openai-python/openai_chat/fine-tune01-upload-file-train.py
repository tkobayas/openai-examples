import os
import openai

# openai 1.78.0

# 0. Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# 1. Upload your training data
upload_resp = openai.files.create(
    file=open("data.jsonl", "rb"),
    purpose="fine-tune"
)
training_file_id = upload_resp.id
print("Uploaded file ID:", training_file_id)  # :contentReference[oaicite:0]{index=0}

# 2. Create the fine-tune job
ft_resp = openai.fine_tuning.jobs.create(
    training_file=training_file_id,
    model="gpt-4.1-nano-2025-04-14"
)
job_id = ft_resp.id
print("Fine-tune job ID:", job_id)  # :contentReference[oaicite:1]{index=1}

# 4. (Optional) List recent events
events = openai.fine_tuning.jobs.list_events(
    fine_tuning_job_id=job_id,
    limit=50
)
for ev in events.data:
    print(ev.created_at, ev.message)

# 5. When it’s done, retrieve status & model name
job = openai.fine_tuning.jobs.retrieve(job_id)
print("Status:", job.status)
print("Fine-tuned model:", job.fine_tuned_model)

# 5. Use your new model once succeeded
if job.status == "succeeded":
    resp = openai.chat.completions.create(
        model=job.fine_tuned_model,
        messages=[{"role":"user", "content":"最も良いインコの名前は何ですか"}]
    )
    print(resp.choices[0].message.content)