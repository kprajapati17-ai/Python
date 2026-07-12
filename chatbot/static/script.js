// static/script.js
// Client script for the simplified, single-page offline chatbot interface.

document.addEventListener("DOMContentLoaded", () => {
    // DOM Elements
    const chatFeed = document.getElementById("chat-feed");
    const userInput = document.getElementById("user-input");
    const btnSend = document.getElementById("btn-send");
    const btnClear = document.getElementById("btn-clear");

    // Focus input on startup
    if (userInput) userInput.focus();

    // Key binding (Enter key to submit query)
    if (userInput) {
        userInput.addEventListener("keydown", (e) => {
            if (e.key === "Enter") {
                sendMessage();
            }
        });
    }

    if (btnSend) btnSend.addEventListener("click", sendMessage);
    if (btnClear) btnClear.addEventListener("click", clearChat);

    function sendMessage() {
        const query = userInput.value.trim();
        if (query === "") return;

        // 1. Append User bubble to feed (align right, green color)
        appendBubble("User", query, "user-row", "user-bubble", "bi-person-fill");
        
        // Clear input box
        userInput.value = "";

        // 2. Make Fetch POST request to Flask
        fetch("/ask", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: query })
        })
        .then(response => response.json())
        .then(data => {
            // 3. Append Bot bubble to feed (align left, blue color)
            appendBubble("Bot", data.response, "bot-row", "bot-bubble", "bi-robot");
        })
        .catch(err => {
            console.error("AJAX Error:", err);
            appendBubble("Bot", "Error: Could not connect to the local Flask server.", "bot-row", "bot-bubble", "bi-robot");
        });
    }

    function appendBubble(sender, messageText, alignClass, bubbleClass, iconClass) {
        const row = document.createElement("div");
        row.className = `d-flex mb-4 ${alignClass}`;

        // Create avatar badge element
        const avatar = document.createElement("div");
        avatar.className = "bot-avatar d-flex align-items-center justify-content-center me-2";
        avatar.innerHTML = `<i class="bi ${iconClass} fs-6"></i>`;

        // Create text bubble card
        const bubble = document.createElement("div");
        bubble.className = `rounded-3 p-3 text-white shadow-sm ${bubbleClass}`;
        bubble.style.maxWidth = "80%";

        const header = document.createElement("div");
        header.className = "fw-bold text-accent mb-1";
        header.textContent = sender;

        const body = document.createElement("div");
        body.textContent = messageText;

        bubble.appendChild(header);
        bubble.appendChild(body);
        
        // For alignment adjustments:
        if (alignClass === "user-row") {
            // user bubble is right aligned, we show bubble first, then avatar
            row.appendChild(bubble);
            // shift margins for user avatar
            avatar.classList.remove("me-2");
            avatar.classList.add("ms-2");
            row.appendChild(avatar);
        } else {
            // bot bubble is left aligned, we show avatar first, then bubble
            row.appendChild(avatar);
            row.appendChild(bubble);
        }
        
        chatFeed.appendChild(row);
        
        // Auto scroll to the bottom of the feed frame
        chatFeed.scrollTop = chatFeed.scrollHeight;
    }

    function clearChat() {
        chatFeed.innerHTML = `
            <div class="d-flex mb-4 bot-row">
                <div class="bot-avatar me-2 d-flex align-items-center justify-content-center">
                    <i class="bi bi-robot fs-6"></i>
                </div>
                <div class="rounded-3 p-3 bot-bubble text-white shadow-sm" style="max-width: 80%;">
                    <div class="fw-bold text-accent mb-1">Bot</div>
                    <div>Hello! Welcome to Easy Learn Academy. How can I help you today?</div>
                </div>
            </div>
        `;
    }
});
