import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000",
});

export const login = async (email, password) => {
  const response = await api.post("/auth/login", { email, password });
  return response.data;
};

export const register = async (email, password, role) => {
  const response = await api.post("/auth/register", { email, password, role });
  return response.data;
};