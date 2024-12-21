import { Card, CardHeader, CardTitle, CardDescription, CardContent } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Github, Server } from "lucide-react"
import './App.css'

function App() {
  return (
    <div className="min-h-screen bg-gray-100 py-8 px-4">
      <div className="max-w-4xl mx-auto">
        <Card className="shadow-lg">
          <CardHeader>
            <CardTitle className="text-2xl">Full Stack Application</CardTitle>
            <CardDescription>Built with modern technologies</CardDescription>
          </CardHeader>
          <CardContent className="space-y-4">
            <div className="flex items-center space-x-4">
              <Server className="text-blue-500" size={24} />
              <div>
                <h3 className="font-medium">Backend Status</h3>
                <p className="text-sm text-gray-500">FastAPI + PostgreSQL</p>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <Github className="text-gray-700" size={24} />
              <div>
                <h3 className="font-medium">Frontend Stack</h3>
                <p className="text-sm text-gray-500">React + Vite + Tailwind</p>
              </div>
            </div>
            <Button className="mt-4" variant="default">
              Check Status
            </Button>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}

export default App
