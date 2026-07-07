function apiPost(url) {
    return fetch(url, { method: "POST" })
        .then(async res => {

            const data = await res.json().catch(() => null);

            if (!res.ok || !data) {
                throw new Error(data?.msg || "Server error");
            }

            return data;
        });
}