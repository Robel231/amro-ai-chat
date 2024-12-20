document.addEventListener("DOMContentLoaded", () => {
    const chatForm = document.getElementById("chat-form");
    const chatBox = document.getElementById("chat-box");
    const userInput = document.getElementById("user-input");

    // Function to append messages to the chat box
    const appendMessage = (message, sender) => {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message", sender);
        messageDiv.textContent = message;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the latest message
    };

    // Handle form submission
    chatForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        const userMessage = userInput.value.trim();

        if (!userMessage) return;

        // Display user's message with "You: " label
        appendMessage(`You: ${userMessage}`, "user");
        userInput.value = "";

        // Display loading indicator for AI response
        appendMessage("Amro AI is thinking...", "loading");

        try {
            // Send user's message to the server
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: userMessage }),
            });

            const data = await response.json();

            // Replace loading indicator with AI's response with "Amro Response: " label
            const loadingMessage = document.querySelector(".message.loading");
            if (loadingMessage) loadingMessage.remove();

            if (data.response) {
                appendMessage(data.response, "ai");
            } else if (data.error) {
                appendMessage(`Amro Response: ${data.error}`, "ai");
            }
        } catch (error) {
            console.error("Error:", error);
            // Replace loading indicator with an error message
            const loadingMessage = document.querySelector(".message.loading");
            if (loadingMessage) loadingMessage.remove();

            appendMessage("Amro Response: Oops! Something went wrong. Please try again.", "ai");
        }
    });
});
