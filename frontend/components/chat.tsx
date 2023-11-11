'use client'

import { useChat, type Message } from 'ai/react'

import { cn } from '@/lib/utils'
import { ChatList } from '@/components/chat-list'
import { ChatPanel } from '@/components/chat-panel'
import { EmptyScreen } from '@/components/empty-screen'
import { ChatScrollAnchor } from '@/components/chat-scroll-anchor'
import { useLocalStorage } from '@/lib/hooks/use-local-storage'
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle
} from '@/components/ui/dialog'
import { useState } from 'react'
import { Button } from './ui/button'
import { Input } from './ui/input'
import { toast } from 'react-hot-toast'
import { CreateMessage } from 'ai'
import { getChats } from '@/app/actions'

const IS_PREVIEW = process.env.VERCEL_ENV === 'preview'
export interface ChatProps extends React.ComponentProps<'div'> {
  initialMessages?: Message[]
  id?: string
}

export function Chat({ id, initialMessages, className }: ChatProps) {
  const [previewToken, setPreviewToken] = useLocalStorage<string | null>(
    'ai-token',
    null
  )
  const [previewTokenDialog, setPreviewTokenDialog] = useState(IS_PREVIEW)
  const [previewTokenInput, setPreviewTokenInput] = useState(previewToken ?? '')
  // const { messages, append, reload, stop, isLoading, input, setInput } =
  //   useChat({
  //     initialMessages,
  //     id,
  //     body: {
  //       id,
  //       previewToken
  //     },
  //     onResponse(response) {
  //       if (response.status === 401) {
  //         toast.error(response.statusText)
  //       }
  //     }
  //   })
  const [messages, setMessages] = useState<Message[]>([])
  const [input, setInput] = useState<string>('')
  const [isLoading, setIsLoading] = useState<boolean>(false)
  const stop = () => {
    console.log('stop was pressed')
  }
  const reload = async () => {
    console.log('reload was pressed')
    await new Promise(resolve => setTimeout(resolve, 1000))
    return undefined
  }

  const append = async (message: Message | CreateMessage) => {
    setMessages(messages => [
      ...messages,
      { ...message, role: 'user' } as Message
    ])

    window.scrollTo({
      top: document.documentElement.scrollHeight,
      behavior: 'smooth'
    })

    async function postMessage(text: string): Promise<any> {
      const rooturl = 'http://94.237.15.54:5000'

      const response = await fetch(`${rooturl}/api/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Access-Control-Allow-Origin': '*'
        },
        body: JSON.stringify({ text, number_of_links: 2 })
      })
      console.log(response, 'response')
      return await response.json()
    }

    setIsLoading(true)
    const response = await postMessage(message.content ?? 'yoyoyoy')
    setIsLoading(false)

    setMessages(messages => [
      ...messages,
      {
        id: Math.random().toString(),
        content: response.output ?? 'Failed to generate response',
        role: 'system',
        createdAt: new Date()
      }
    ])

    window.scrollTo({
      top: document.documentElement.scrollHeight,
      behavior: 'smooth'
    })

    return message.content ?? 'yoyoyoy'
  }

  console.log(messages, 'messages')

  return (
    <>
      <div className={cn('pb-[200px] pt-4 md:pt-10', className)}>
        {messages.length ? (
          <>
            <ChatList messages={messages} />
            <ChatScrollAnchor trackVisibility={isLoading} />
          </>
        ) : (
          <EmptyScreen setInput={setInput} />
        )}
      </div>
      <ChatPanel
        id={id}
        isLoading={isLoading}
        stop={stop}
        append={append}
        reload={reload}
        messages={messages}
        input={input}
        setInput={setInput}
      />

      <Dialog open={previewTokenDialog} onOpenChange={setPreviewTokenDialog}>
        <DialogContent>
          <DialogHeader>
            <DialogTitle>Enter your OpenAI Key</DialogTitle>
            <DialogDescription>
              If you have not obtained your OpenAI API key, you can do so by{' '}
              <a
                href="https://platform.openai.com/signup/"
                className="underline"
              >
                signing up
              </a>{' '}
              on the OpenAI website. This is only necessary for preview
              environments so that the open source community can test the app.
              The token will be saved to your browser&apos;s local storage under
              the name <code className="font-mono">ai-token</code>.
            </DialogDescription>
          </DialogHeader>
          <Input
            value={previewTokenInput}
            placeholder="OpenAI API key"
            onChange={e => setPreviewTokenInput(e.target.value)}
          />
          <DialogFooter className="items-center">
            <Button
              onClick={() => {
                setPreviewToken(previewTokenInput)
                setPreviewTokenDialog(false)
              }}
            >
              Save Token
            </Button>
          </DialogFooter>
        </DialogContent>
      </Dialog>
    </>
  )
}
