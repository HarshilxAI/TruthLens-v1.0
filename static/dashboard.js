document.addEventListener("DOMContentLoaded", () => {

    // =====================================
    // IMAGE PREVIEW
    // =====================================

    const imageInput =
        document.getElementById("imageInput");

    const previewImage =
        document.getElementById("previewImage");

    if (imageInput && previewImage) {

        imageInput.addEventListener("change", (e) => {

            const file = e.target.files[0];

            if (file) {

                previewImage.src =
                    URL.createObjectURL(file);

                previewImage.style.display =
                    "block";

            }

        });

    }

    // =====================================
    // CONFIDENCE GAUGE
    // =====================================

    const progressCircle =
        document.querySelector(".progress-circle");

    if (progressCircle) {

        const confidence =
            parseFloat(
                progressCircle.dataset.confidence
            );

        const radius = 50;

        const circumference =
            2 * Math.PI * radius;

        progressCircle.style.strokeDasharray =
            circumference;

        progressCircle.style.strokeDashoffset =
            circumference;

        const offset =
            circumference -
            (confidence / 100) * circumference;

        setTimeout(() => {

            progressCircle.style.transition =
                "stroke-dashoffset 1.5s ease";

            progressCircle.style.strokeDashoffset =
                offset;

        }, 300);

    }

    // =====================================
    // DRAG & DROP EFFECT
    // =====================================

    const uploadContent =
        document.querySelector(".upload-content");

    if (uploadContent) {

        uploadContent.addEventListener("dragover", (e) => {

            e.preventDefault();

            uploadContent.style.borderColor =
                "#00E5FF";

            uploadContent.style.transform =
                "translateY(-5px)";

        });

        uploadContent.addEventListener("dragleave", () => {

            uploadContent.style.borderColor =
                "rgba(255,255,255,.06)";

            uploadContent.style.transform =
                "translateY(0px)";

        });

        uploadContent.addEventListener("drop", () => {

            uploadContent.style.borderColor =
                "rgba(255,255,255,.06)";

            uploadContent.style.transform =
                "translateY(0px)";

        });

    }

    // =====================================
    // CARD HOVER EFFECTS
    // =====================================

    const cards =
        document.querySelectorAll(
            ".dashboard-card, .analysis-card"
        );

    cards.forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform =
                "translateY(-5px)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform =
                "translateY(0px)";

        });

    });

    // =====================================
    // FULLSCREEN IMAGE MODAL
    // =====================================

    const images =
        document.querySelectorAll(
            ".analysis-image"
        );

    const modal =
        document.getElementById(
            "imageModal"
        );

    const modalImage =
        document.getElementById(
            "modalImage"
        );

    const closeModal =
        document.querySelector(
            ".close-modal"
        );

    if (images.length > 0 &&
        modal &&
        modalImage &&
        closeModal) {

        images.forEach(img => {

            img.addEventListener("click", () => {

                modal.style.display =
                    "block";

                modalImage.src =
                    img.src;

            });

        });

        closeModal.addEventListener("click", () => {

            modal.style.display =
                "none";

        });

        modal.addEventListener("click", (e) => {

            if (e.target === modal) {

                modal.style.display =
                    "none";

            }

        });

    }

    // =====================================
    // REPORT BUTTON
    // =====================================

    const reportButton =
        document.querySelector(".report-btn");

    if (reportButton) {

        reportButton.addEventListener("click", () => {

            const reportButton =
document.querySelector(".report-btn");

if(reportButton){

    reportButton.addEventListener("click",()=>{

        alert(
`🔒 PHASE 2 FEATURE

🔒 Generate Forensics Report (Phase 2)

This feature will be unlocked in Phase 2 of TruthLens AI.

Upcoming Features:
• Download PDF Report
• Detection History
• AI Risk Scoring
• Deepfake Classification`
        );

    });

}

            setTimeout(() => {

                notification.remove();

            }, 3000);

        });

    }

});