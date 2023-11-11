import { UseChatHelpers } from 'ai/react'

import { Button } from '@/components/ui/button'
import { ExternalLink } from '@/components/external-link'
import { IconArrowRight } from '@/components/ui/icons'

const exampleMessages = [
  {
    heading:
      'What is the expected development of stainless steel market pricing for a specific alloy in the next month?',
    message: `What is the expected development of stainless steel market pricing for a specific alloy in the next month \n?`
  },
  {
    heading:
      'What recent news state about possible energy price developments over the next three months?',
    message:
      'What recent news state about possible energy price developments over the next three months? \n'
  },
  {
    heading:
      'What are the most recent patents granted in the area of stainless steel manufacturing?',
    message: `What are the most recent patents granted in the area of stainless steel manufacturing? \n`
  }
]

export function EmptyScreen({ setInput }: Pick<UseChatHelpers, 'setInput'>) {
  return (
    <div className="mx-auto max-w-2xl px-4">
      <div className="rounded-lg border bg-background p-8">
        <h1 className="mb-2 text-lg font-semibold">Welcome to SteelGPT</h1>
        <p className="leading-normal text-muted-foreground">
          SteelGPT offers real-time insights into the steel industry by
          utilizing the latest data from credible sources.
        </p>
        <div className="mt-4 flex flex-col items-start space-y-2">
          {exampleMessages.map((message, index) => (
            <Button
              key={index}
              variant="link"
              className="h-auto p-0 text-base"
              onClick={() => setInput(message.message)}
            >
              <IconArrowRight className="mr-2 text-muted-foreground" />
              {message.heading}
            </Button>
          ))}
        </div>
      </div>
    </div>
  )
}
