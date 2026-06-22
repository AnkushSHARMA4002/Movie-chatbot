from app.memory.memory import save_message

save_message(
    user_id="1",
    conversation_id="abc123",
    role="user",
    content="Hello"
)

print("Saved")