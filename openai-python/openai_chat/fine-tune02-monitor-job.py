import os
import openai

# openai 1.78.0

# 0. Set your API key
openai.api_key = os.getenv("OPENAI_API_KEY")

job_id = "ftjob-dryy2cjs6M0pscdFGTdSQxsk" # replace with the job_id found in the previous fine-tune01 run

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
print(job)

# 5. Use your new model once succeeded
if job.status == "succeeded":
    resp = openai.chat.completions.create(
        model=job.fine_tuned_model,
        messages=[{"role":"user", "content":"最も良いインコの名前は何ですか"}]
    )
    print(resp.choices[0].message.content)
